import cv2
import gradio as gr
import numpy as np
from PIL import Image
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

def process_image(image):
    # 이미지를 OpenCV 형식으로 변환
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 모델로 객체 검출 수행
    results = model(image)

    # 결과에서 박스와 레이블을 추출하여 그리기
    for result in results[0].boxes:  # 결과는 results[0].boxes에 저장됩니다
        # 바운딩 박스 좌표 및 신뢰도, 클래스 ID 추출
        xyxy = result.xyxy[0]  # [x1, y1, x2, y2] 좌표 (Tensor 형태)
        confidence = result.conf[0].item()  # 신뢰도
        class_id = result.cls[0].item()  # 클래스 ID

        # 클래스 이름을 가져오기
        label = results[0].names[int(class_id)]  # 객체 이름 추출 (클래스 ID로부터)

        # 바운딩 박스를 그리기
        x1, y1, x2, y2 = map(int, xyxy.tolist())  # 좌표를 정수로 변환
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Bounding box 그리기
        cv2.putText(image, f"{label} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  # 레이블 추가

    # BGR 이미지를 RGB로 변환하여 PIL 이미지로 반환
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(image)

# Gradio 인터페이스 설정
iface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="pil"),
    outputs="image",
    title="Vision AI Object Detection",
    description="Upload an image to detect objects using YOLOv8.",
)

# 인터페이스 실행
iface.launch(share=True)
