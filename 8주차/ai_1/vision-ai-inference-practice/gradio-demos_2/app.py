import cv2
import gradio as gr
import requests
import numpy as np
from PIL import Image
from requests.auth import HTTPBasicAuth


# 가상의 비전 AI API URL (예: 객체 탐지 API)
#ver2 - M
#URL = "https://suite-endpoint-api-apne2.superb-ai.com/endpoints/389091e1-940c-473e-9de6-51f7ff117583/inference"

#ver3 - M
#URL = "https://suite-endpoint-api-apne2.superb-ai.com/endpoints/294d7a63-a358-4829-aebe-9562120adb3c/inference"

#ver5 - M
#URL = "https://suite-endpoint-api-apne2.superb-ai.com/endpoints/b99eb756-95d8-4bd5-b147-cfb45fb2d90b/inference"

# ver5 - N
URL = "https://suite-endpoint-api-apne2.superb-ai.com/endpoints/58ac431a-e499-4d30-a6c7-5c39ccd7bfbb/inference"

TEAM = "kdt_2024_1-17"
ACCESS_KEY = "87Ooe3vJlV859berMYnCja8GUJpepPue2SCPwzVl"
total_count = 0
def process_image(image):
    # 이미지를 OpenCV 형식으로 변환
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 이미지를 API에 전송할 수 있는 형식으로 변환
    _, img_encoded = cv2.imencode(".jpg", image)
    
    # API 호출 및 결과 받기 - 실습1
    response = requests.post(
        url=URL,
        auth=HTTPBasicAuth("kdt2024_1-17", ACCESS_KEY),
        headers={"Content-Type": "image/jpeg"},
        data=img_encoded.tobytes(),  # .tobytes()로 byte 형태로 데이터 전달
    )

    
    objects = response.json().get("objects", [])
    i = 20
    name_count = 1
    pre_name = None
    name_dict = {}
    for obj_name in objects:
        name = obj_name['class']
        if name not in name_dict:
            name_dict[name] = 1
        else:
            name_dict[name] += 1
        
    
    # API 결과를 바탕으로 박스 그리기 - 실습2
    for obj in objects:
        name = obj['class']
        start_point = (obj['box'][0], obj['box'][1])
        end_point = (obj['box'][2], obj['box'][3])
        color = (0, 255, 0)  # BGR 색상 (초록색)
        thickness = 2  # 박스 선의 두께
        # 박스 그리기   
        cv2.rectangle(image, start_point, end_point, color, thickness)
        
        text = name
        position = (obj['box'][0], obj['box'][1] - 20)  # 텍스트 시작 위치 (x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX  # 글꼴 설정
        font_scale = 0.4  # 글자 크기
        color_names = (0, 255, 0)
        thickness = 1  # 글자 두께
        cv2.putText(image, text, position, font, font_scale, color_names, thickness, cv2.LINE_AA)

    for key in name_dict:
        text = f'{key} x {name_dict[key]}'
        position = (0, i) # 텍스트 시작 위치 (x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX # 글꼴 설정
        font_scale = 0.5 # 글자 크기
        color_names = (255, 0, 0)
        thickness = 1 # 글자 두께
        i+=20
        cv2.putText(image, text, position, font, font_scale, color_names, thickness, cv2.LINE_AA)


    # BGR 이미지를 RGB로 변환
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(image)

# Gradio 인터페이스 설정
iface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="pil"),
    outputs="image",
    title="Vision AI Object Detection",
    description="Upload an image to detect objects using Vision AI.",
)

# 인터페이스 실행
iface.launch(share=True)
