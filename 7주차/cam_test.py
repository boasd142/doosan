import rclpy, random
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy, QoSDurabilityPolicy, Duration
import cv2
import numpy as np

class CompressedImageNode(Node):
    def __init__(self):
        super().__init__('compressed_image_node')

        # CvBridge 초기화
        self.bridge = CvBridge()

        # QoS 설정
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10,
            durability=QoSDurabilityPolicy.VOLATILE
        )

        # ROS 2 이미지 구독
        self.subscription = self.create_subscription(
            CompressedImage,
            '/oakd/rgb/preview/image_raw/compressed',
            self.listener_callback,
            qos_profile
        )

        # SIFT 특징점 검출기 초기화
        self.sift = cv2.SIFT_create()

        # 첫 번째 이미지 로드
        self.img1 = cv2.imread('/home/bok/Downloads/man_orig.png', cv2.IMREAD_GRAYSCALE)
        self.img2 = cv2.imread('/home/bok/Downloads/ext_orig.png', cv2.IMREAD_GRAYSCALE)
        if self.img1 is None or self.img2 is None:
            self.get_logger().error("원본 이미지를 로드하지 못했습니다.")
            return

        self.keypoints1, self.descriptors1 = self.sift.detectAndCompute(self.img1, None)
        self.keypoints2, self.descriptors2 = self.sift.detectAndCompute(self.img2, None)

        # Optical Flow 초기화
        self.prev_gray1, self.prev_gray2 = None, None
        self.prev_points1, self.prev_points2 = None, None
        self.random_colors1, self.random_colors2 = None, None
        self.tracked_lines_human, self.tracked_lines_ext = [], []
        self.matching1, self.matching2 = True, True

        # Optical Flow 파라미터
        self.feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)
        self.lk_params = dict(winSize=(15, 15), maxLevel=2,
                              criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    def listener_callback(self, msg):
        try:
            frame = self.bridge.compressed_imgmsg_to_cv2(msg)
        except Exception as e:
            self.get_logger().error(f"이미지 변환 오류: {e}")
            return

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        keypoints_frame, descriptors_frame = self.sift.detectAndCompute(gray, None)

        if descriptors_frame is not None:
            index_params = dict(algorithm=1, trees=5)
            search_params = dict(checks=50)
            flann = cv2.FlannBasedMatcher(index_params, search_params)

            matches1 = flann.knnMatch(descriptors_frame, self.descriptors1, k=2)
            matches2 = flann.knnMatch(descriptors_frame, self.descriptors2, k=2)

            good_matches1 = [m for m, n in matches1 if m.distance < 0.4 * n.distance]
            good_matches2 = [m for m, n in matches2 if m.distance < 0.6 * n.distance]

            self.match_mode1(frame, good_matches1, keypoints_frame)
            self.match_mode2(frame, good_matches2, keypoints_frame)

            if not self.matching1:
                self.optical_flow_human(frame, gray)
            if not self.matching2:
                self.optical_flow_ext(frame, gray)
        else:
            self.match_mode1(frame, [], None)
            self.match_mode2(frame, [], None)

        self.prev_gray1 = gray
        self.prev_gray2 = gray


    def match_mode1(self, frame, good_matches1, keypoints_frame):
        if len(good_matches1) > 40:
            self.matching1 = False
            print("사람 발견")
        # 매칭 결과가 없어도 창 표시
        if keypoints_frame is not None:
            frame_matches1 = cv2.drawMatches(frame, keypoints_frame, self.img1, self.keypoints1,
                                            good_matches1, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        else:
            frame_matches1 = frame  # 기본 프레임만 표시

        cv2.imshow('Check Human', frame_matches1)
        cv2.waitKey(1)


    def match_mode2(self, frame, good_matches2, keypoints_frame):
        if len(good_matches2) > 20:
            self.matching2 = False
            print("소화기 발견")
        # 매칭 결과가 없어도 창 표시
        if keypoints_frame is not None:
            frame_matches2 = cv2.drawMatches(frame, keypoints_frame, self.img2, self.keypoints2,
                                            good_matches2, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        else:
            frame_matches2 = frame  # 기본 프레임만 표시

        cv2.imshow('Check Ext', frame_matches2)
        cv2.waitKey(1)


    def optical_flow_human(self, frame, gray):
        max_lines = 100
        if self.prev_points1 is None:
            self.prev_points1 = cv2.goodFeaturesToTrack(gray, mask=None, **self.feature_params)
            if self.prev_points1 is not None:
                self.random_colors1 = [tuple(random.randint(0, 255) for _ in range(3))
                                       for _ in range(len(self.prev_points1))]

        if self.prev_points1 is not None:
            next_pts, status, _ = cv2.calcOpticalFlowPyrLK(self.prev_gray1, gray, self.prev_points1, None, **self.lk_params)
            if next_pts is None or len(next_pts[status == 1]) == 0:
            # 추적 점이 사라지면 창 닫기 및 상태 초기화
                if cv2.getWindowProperty('Optical Flow Human', cv2.WND_PROP_VISIBLE) >= 1:
                    print("Optical Flow Human: 추적 점이 사라짐")
                    self.matching1 = True
                    self.prev_points1 = None
                    self.tracked_lines_human.clear()
                    cv2.destroyWindow('Optical Flow Human')
                return
            good_new = next_pts[status == 1]
            good_old = self.prev_points1[status == 1]
            for (new, old), color in zip(zip(good_new, good_old), self.random_colors1):
                a, b = new.ravel()
                c, d = old.ravel()
                self.tracked_lines_human.append(((int(a), int(b)), (int(c), int(d)), color))
                if len(self.tracked_lines_human) > max_lines:
                    self.tracked_lines_human = self.tracked_lines_human[-max_lines:]
            for (start, end, color) in self.tracked_lines_human:
                cv2.line(frame, start, end, color, 2)
            self.prev_points1 = good_new.reshape(-1, 1, 2)

        cv2.imshow('Optical Flow Human', frame)
        cv2.waitKey(1)

    def optical_flow_ext(self, frame, gray):
        max_lines = 100
        if self.prev_points2 is None:
            self.prev_points2 = cv2.goodFeaturesToTrack(gray, mask=None, **self.feature_params)
            if self.prev_points2 is not None:
                self.random_colors2 = [tuple(random.randint(0, 255) for _ in range(3))
                                       for _ in range(len(self.prev_points2))]

        if self.prev_points2 is not None:
            next_pts, status, _ = cv2.calcOpticalFlowPyrLK(self.prev_gray2, gray, self.prev_points2, None, **self.lk_params)
            if next_pts is None or len(next_pts[status == 1]) == 0:
                # 추적 점이 사라지면 창 닫기 및 상태 초기화
                if cv2.getWindowProperty('Optical Flow Ext', cv2.WND_PROP_VISIBLE) >= 1:
                    print("Optical Flow Ext: 추적 점이 사라짐")
                    self.matching2 = True
                    self.prev_points2 = None
                    self.tracked_lines_ext.clear()
                    cv2.destroyWindow('Optical Flow Ext')
                return            
            good_new = next_pts[status == 1]
            good_old = self.prev_points2[status == 1]
            for (new, old), color in zip(zip(good_new, good_old), self.random_colors2):
                a, b = new.ravel()
                c, d = old.ravel()
                self.tracked_lines_ext.append(((int(a), int(b)), (int(c), int(d)), color))
                if len(self.tracked_lines_ext) > max_lines:
                    self.tracked_lines_ext = self.tracked_lines_ext[-max_lines:]
            for (start, end, color) in self.tracked_lines_ext:
                cv2.line(frame, start, end, color, 2)
            self.prev_points2 = good_new.reshape(-1, 1, 2)

        cv2.imshow('Optical Flow Ext', frame)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)
    node = CompressedImageNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
