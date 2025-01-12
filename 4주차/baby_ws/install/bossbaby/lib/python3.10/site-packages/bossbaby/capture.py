import cv2
import os

save_directory = "img_capture"  # 저장 디렉토리 설정

def capture_video_and_extract_frames():
    os.makedirs(save_directory, exist_ok=True)

    # 웹캠 비디오 캡처
    cap = cv2.VideoCapture(2)  # PC 카메라 (웹캠)

    if not cap.isOpened():
        print("Error: 카메라를 열 수 없습니다.")
        return

    image_count = 0
    recording = False  # 녹화 상태 추적
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # 카메라에서 프레임을 못 읽으면 종료

        # 비디오 화면 출력
        cv2.imshow("Webcam", frame)

        # 's' 키를 누르면 녹화 시작
        if cv2.waitKey(1) & 0xFF == ord('s'):
            if not recording:  # 녹화가 시작되지 않은 경우에만 시작
                recording = True
                print("녹화가 시작되었습니다.")

        # 녹화 중일 때 프레임 저장
        if recording:
            if image_count < 1000:
                file_name = f'{save_directory}/frame_{image_count}.jpg'
                cv2.imwrite(file_name, frame)  # 프레임을 이미지로 저장
                print(f"Image saved: {file_name}")
                image_count += 1

            # 1000프레임을 추출하면 종료
            if image_count >= 1000:
                break

        # 'q' 키를 누르면 촬영 종료
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # 카메라 캡처 해제
    cv2.destroyAllWindows()

def main():
    print("비디오 촬영을 시작하려면 's' 키를 누르세요.")
    capture_video_and_extract_frames()  # 비디오 촬영 및 프레임 추출

if __name__ == "__main__":
    main()