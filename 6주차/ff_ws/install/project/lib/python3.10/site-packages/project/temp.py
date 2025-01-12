import cv2
#from ultralytics import YOLO

# 모델 로드 (로컬 경로에서 best.pt 로드)
#model = YOLO('/home/woojng/Desktop/best/best.pt')  # best.pt 경로 지정

# 웹캠 열기
cap = cv2.VideoCapture(2)  # 기본 웹캠 (0번)

# 웹캠이 열리지 않으면 오류 출력
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    # 웹캠에서 프레임 읽기
    ret, frame = cap.read()

    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # 객체 인식 (모델에 프레임 입력)
    #results = model(frame)

    # 결과 처리 (객체 인식 결과 렌더링)
    #frame = results[0].plot()  # 결과 이미지를 렌더링


    # 화면에 결과 출력
    cv2.imshow("Object Detection", frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 종료 및 창 닫기
cap.release()
cv2.destroyAllWindows()

