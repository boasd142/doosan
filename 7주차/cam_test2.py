import cv2
import numpy as np

# 비디오 캡처
cap = cv2.VideoCapture(0)

# 첫 번째 프레임 읽기
ret, frame = cap.read()
if not ret:
    print("비디오 캡처 실패")
    cap.release()
    exit()

# 첫 번째 프레임을 그레이스케일로 변환
old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 첫 번째 프레임에서 특징점 찾기
feature_params = dict(maxCorners=100, qualityLevel=0.5, minDistance=7, blockSize=7)
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# 모든 특징점에 동일한 색상 할당 (예: 빨간색)
if p0 is not None:
    point_colors = np.array([[0, 0, 255]] * len(p0))  # 빨간색 (BGR)

# 최대 특징점 개수 설정
MAX_FEATURES = 100
MIN_DISTANCE = 30  # 새 특징점이 기존 점과 너무 가까운 경우 제외할 거리

# 이전 특징점 위치를 저장하기 위한 리스트
all_points = []  # 모든 점들을 저장하여 추적

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # 현재 프레임을 그레이스케일로 변환
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 옵티컬 플로우 계산
    p1, status, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None)

    if p1 is None or status is None:  # 옵티컬 플로우 계산 실패시
        print("옵티컬 플로우 계산 실패")
        p0 = cv2.goodFeaturesToTrack(frame_gray, mask=None, **feature_params)  # 새 특징점 찾기
        if p0 is not None:
            point_colors = np.array([[0, 0, 255]] * len(p0))  # 새 특징점에 대해 빨간색 할당
        continue
    
    # 상태(status)를 1D로 평탄화
    status = status.reshape(-1)

    # 추적 성공한 특징점
    good_new = p1[status == 1].reshape(-1, 2)
    good_old = p0[status == 1].reshape(-1, 2)

    # point_colors 크기를 good_new에 맞게 조정
    point_colors = np.array([[0, 0, 255]] * len(good_new))  # 추적 성공한 특징점에 대해 색상 재할당

    # 새로 들어온 특징점 찾기
    p0_new = cv2.goodFeaturesToTrack(frame_gray, mask=None, **feature_params)
    new_points = []
    if p0_new is not None:
        p0_new = p0_new.reshape(-1, 2)  # (n, 2) 형태로 변경

        # 기존 특징점과 너무 가까운 위치의 특징점은 제외
        for new_point in p0_new:
            is_near_existing = False
            for old_point in good_new:
                if np.linalg.norm(new_point - old_point) < MIN_DISTANCE:
                    is_near_existing = True
                    break
            if not is_near_existing:
                new_points.append(new_point)

        # 새 특징점 추가
        if new_points:
            # 기존 특징점과 새로운 특징점 합치기
            combined_points = np.vstack((good_new, np.array(new_points)))
            if len(combined_points) > MAX_FEATURES:
                p0 = combined_points[:MAX_FEATURES]  # 최대 특징점 개수 제한
            else:
                p0 = combined_points
        else:
            p0 = good_new
    else:
        p0 = good_new  # 새 특징점이 없으면 기존 점들로 계속 진행

    # 모든 특징점에 대해 이전 위치와 새로운 위치를 연결하는 선 그리기
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        frame = cv2.line(frame, (int(a), int(b)), (int(c), int(d)), point_colors[i].tolist(), 2)

    # 기존 특징점 그리기
    for i, (new) in enumerate(good_new):
        a, b = new.ravel()
        frame = cv2.circle(frame, (int(a), int(b)), 5, point_colors[i].tolist(), -1)

    # 새로 추가된 특징점 그리기 (circle로만)
    if new_points:
        for i, new in enumerate(new_points):
            a, b = new
            frame = cv2.circle(frame, (int(a), int(b)), 5, point_colors[i].tolist(), -1)

    # 결과 보여주기
    cv2.imshow('Optical Flow Tracking', frame)

    # 종료 조건
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # 이전 상태 업데이트
    old_gray = frame_gray.copy()

    # all_points에 현재 상태를 추가 (기존 점들 업데이트)
    all_points.append(good_new)

    # 새로운 특징점 리스트로 p0 갱신
    p0 = np.vstack((good_new, np.array(new_points))) if new_points else good_new

cap.release()
cv2.destroyAllWindows()
