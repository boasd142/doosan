import os
import requests
from requests.auth import HTTPBasicAuth

path = '/home/bok/Downloads/test_img'
# ver5 - N
#URL = "https://suite-endpoint-api-apne2.superb-ai.com/endpoints/58ac431a-e499-4d30-a6c7-5c39ccd7bfbb/inference"
# ver5 - M
URL = "https://suite-endpoint-api-apne2.superb-ai.com/endpoints/b99eb756-95d8-4bd5-b147-cfb45fb2d90b/inference"
ACCESS_KEY = "87Ooe3vJlV859berMYnCja8GUJpepPue2SCPwzVl"

# 확장자가 .jpg인 파일들의 리스트 생성
jpg_files = [f for f in os.listdir(path) if f.endswith('.jpg')]

missing_counts = {key: 0 for key in ['RASPBERRY PICO', 'CHIPSET', 'BOOTSEL', 'USB', 'HOLE', 'OSCILLIATOR']}
miss = 0
total_count = 0
for images in jpg_files:
    total_count += 1
    # 이미지 이름에서 숫자 추출
    image_number = int(''.join(filter(str.isdigit, images)))

    # 이미지 번호가 20에서 99 사이가 아니면 건너뜀
    if not (20 <= image_number <= 99):
        continue

    IMAGE_FILE_PATH = os.path.join(path, images)
    with open(IMAGE_FILE_PATH, "rb") as img_file:
        image = img_file.read()

    response = requests.post(
        url=URL,
        auth=HTTPBasicAuth("kdt2024_1-17", ACCESS_KEY),
        headers={"Content-Type": "image/jpeg"},
        data=image,
    )

    objects = response.json().get("objects", [])

    name_dict = {}
    for obj_name in objects:
        name = obj_name['class']
        name_dict[name] = name_dict.get(name, 0) + 1

    required_keys = ['RASPBERRY PICO', 'CHIPSET', 'BOOTSEL', 'USB', 'HOLE', 'OSCILLIATOR']

    # 누락된 키 확인 및 카운트 증가
    for key in required_keys:
        if key not in name_dict:
            missing_counts[key] += 1

    # 조건 확인: HOLE이 4가 아니거나 다른 객체가 1이 아닌 경우 또는 키가 누락된 경우
    if ('HOLE' not in name_dict or name_dict['HOLE'] != 4) or \
       any(name_dict.get(key, 0) != 1 for key in required_keys if key != 'HOLE'):
        print(f"Image: {images}")
        print(f"Objects: {name_dict}")
        print("-" * 50)
        miss += 1


# 누락된 키에 대한 총 카운트 출력
print("Missing key counts:")
for key, count in missing_counts.items():
    print(f"{key}: {count}")

print(miss)
print(total_count)
