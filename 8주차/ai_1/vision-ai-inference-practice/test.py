import cv2
import requests
import numpy as np
from requests.auth import HTTPBasicAuth

# Vision AI API 설정
# ver5 - M
#URL = "https://suite-endpoint-api-apne2.superb-ai.com/endpoints/b99eb756-95d8-4bd5-b147-cfb45fb2d90b/inference"

# ver5 - N
URL = "https://suite-endpoint-api-apne2.superb-ai.com/endpoints/58ac431a-e499-4d30-a6c7-5c39ccd7bfbb/inference"
TEAM = "kdt_2024_1-17"
ACCESS_KEY = "87Ooe3vJlV859berMYnCja8GUJpepPue2SCPwzVl"

# 크롭할 영역 설정
crop_info = {"x": 300, "y": 0, "width": 400, "height": 300}

def detect_objects(frame):
    # 크롭된 이미지로 변환
    cropped_frame = frame[crop_info["y"]:crop_info["y"] + crop_info["height"],
                          crop_info["x"]:crop_info["x"] + crop_info["width"]]

    # 이미지를 API 호출용으로 인코딩
    _, img_encoded = cv2.imencode(".jpg", cropped_frame)
    # 인증을 위한 헤더 추가 (Bearer 인증 방식 예시)
    response = requests.post(
        url=URL,
        auth=HTTPBasicAuth("kdt2024_1-17", ACCESS_KEY),
        headers={"Content-Type": "image/jpeg"},
        data=img_encoded.tobytes(),
    )
    
    # 응답 처리
    if response.status_code == 200:
        return response.json().get("objects", [])
    else:
        print(f"API Error: {response.status_code}, {response.text}")
        return []

def draw_boxes(frame, objects):
    name_dict = {}
    for obj in objects:
        # 클래스명과 박스 정보 가져오기
        name = obj['class']
        start_point = (obj['box'][0], obj['box'][1])
        end_point = (obj['box'][2], obj['box'][3])
        
        # 크롭된 영역에 맞게 바운딩 박스 위치 보정
        start_point = (start_point[0] + crop_info["x"], start_point[1] + crop_info["y"])
        end_point = (end_point[0] + crop_info["x"], end_point[1] + crop_info["y"])

        # 클래스별 개수 카운트
        if name not in name_dict:
            name_dict[name] = 1
        else:
            name_dict[name] += 1

        # Bounding Box 그리기
        color = (0, 255, 0)  # 초록색
        thickness = 2
        cv2.rectangle(frame, start_point, end_point, color, thickness)
        
        # 클래스 이름 텍스트 그리기
        text = name
        position = (start_point[0], start_point[1] - 10)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        text_color = (0, 255, 0)
        text_thickness = 1
        cv2.putText(frame, text, position, font, font_scale, text_color, text_thickness, cv2.LINE_AA)

    # 클래스별 개수 텍스트 그리기
    y_offset = 20
    for key, count in name_dict.items():
        text = f"{key} x {count}"
        position = (10, y_offset)
        cv2.putText(frame, text, position, font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
        y_offset += 20

def main():
    # 웹캠 또는 동영상 파일 열기
    cap = cv2.VideoCapture(0)  # 0은 기본 웹캠, 파일 경로를 전달하면 영상 파일 열기 가능
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # 객체 탐지
        objects = detect_objects(frame)
        
        # 결과에 따라 Bounding Box 그리기
        draw_boxes(frame, objects)

        # 프레임 디스플레이
        cv2.imshow("Real-Time Object Detection", frame)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 자원 해제
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()