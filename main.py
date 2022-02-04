#예외 강제 발생
def ten_div(x):
    if x>10:
        #강제로 예외를 발생시켜서 아래 문장을 수행하지 않음
        raise Exception("숫자가 너무 큽니다")
    return 10/x

#기본적인 예외 처리 구문을 이용해서 예외가 발생하더라도 중지되지 않도록 함
try:
    print(ten_div(2))
    print(ten_div(15)) #예외가 발생해서 프로그램이 중단
#예외가 발생했을 때 예외 메시지 출력
except Exception as e:
    print(e)

else:
    print('예외가 발생하지 않은 경우 수행')

finally:
    print('프로그램 종료')


#일반 함수 호출
import threading, time
def threadEx(id):
    for i in range(10):
        print('id={0} --> {1}'.format(id, i))
        time.sleep(1)

for i in range(2):
    id = ("{0}번 스레드".format(i))
    th = threading.Thread(target=threadEx, args=(id,))  # 쓰레드 함수를 target인수로, 쓰레드로 전달될 인수를 args인수에 전달
    th.start()
print("메인 종료")          # 쓰레드 실행 시작

#singer.csv 읽기
import csv
with open('./data/data/singer.csv', 'r') as f:
    content = f.read()
    data = content.split(',')
    print(type(data))
    for imsi in data:
        print(imsi)


# csv 모듈을 이용해서 읽기 - csv.reader(file객체)를 대입해서 읽음
# 줄 바꿈 별로 하나의 list를 별도로 생성
import csv

with open('./data/data/singer.csv', 'r') as f:
    # CSV로 읽기
    # 구분자가 ,가 아니면 delimiter에 구분자를 설정해주면 됨
    data = csv.reader(f)
    print(type(data))  # 자료형 확인
    # 전체 출력
    for imsi in data:
        print(imsi)