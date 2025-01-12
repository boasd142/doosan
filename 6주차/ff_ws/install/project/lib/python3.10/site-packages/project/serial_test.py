import serial.tools.list_ports
import serial
import time



def check_port_usage(port):
    try:
        # 시리얼 포트 열기 시도
        arduino = serial.Serial(port, baudrate=115200, timeout=1)
        if arduino.isOpen():
            print(f"{port} 포트가 열렸습니다.")
            arduino.close()  # 포트를 사용한 후 닫기
        else:
            print(f"{port} 포트를 열 수 없습니다.")
    except serial.SerialException as e:
        print(f"{port} 포트에서 예외 발생: {e}")

def check_all_ports():
    # 연결된 모든 포트 확인
    ports = serial.tools.list_ports.comports()
    for port in ports:
        check_port_usage(port.device)

# 시스템에 연결된 모든 시리얼 포트 상태 확인
ports = [port.device for port in serial.tools.list_ports.comports()]
print(ports)
#arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

# 아두이노와의 연결이 준비될 때까지 잠시 대기
#time.sleep(2)

'''while True:
    # '1000' 값을 아두이노로 전송
    arduino.write('1000'.encode()+b'\n')  # '1000'을 바이트 형식으로 전송
    print('Sent: 1000')

    time.sleep(1)  # 1초 간격으로 계속 전송
'''