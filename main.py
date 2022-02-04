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


#기록하기
import csv
#newline옵션을 이용해서 빈줄이 생기지 않도록 설정
with open('./data/data/singer.csv', 'a' , newline='') as f:
    #CSV로 읽기
    wr = csv.writer(f)
    wr.writerow([4, 'zkfls', '1991-05-30', 'aespa'])

#바이트 단위로 파일에 읽고 쓰기
with open('./data/test.bin', 'wb') as f:
    f.write("안녕하세요".encode())

#문자열을 바이트 단위로 기록했으므로 읽을 때는 문자열로 변환해서 읽어야 함
with open('./data/test.bin', 'rb') as f:
    byteAr = f.read()
    #print(byteAr)
    print(byteAr.decode())


##Serializable(직렬화)-객체 단위로 파일에 읽고 쓰는 것
# 직렬화를 위해 DTO클래스 생성
class DTO:
    def setNum(self, num):
        self.num = num

    def setName(self, name):
        self.name = name

    def getNum(self):
        return self.num

    def getName(self):
        return self.name

    def toString(self):
        return "{번호:{0} 이름:{1}}".format(self.num, self.name)


# 직렬화 할 인스턴스 생성
dto1 = DTO()
dto1.setNum(1)
dto1.setName("유관순")

dto2 = DTO()
dto2.setNum(2)
dto2.setName("안중근")

li = [dto1, dto2]

import pickle

with open('./data/data.dat', 'wb') as f:
    pickle.dump(li, f)


#객체 직렬화 – 직렬화
import pickle
try:
    with open('./data/test.txt', 'wb') as f:
        pickle.dump(li, f)
        f.close()
    with open('./data/test.txt', 'rb') as f:
        result = pickle.load(f)
        for temp in result:
            print(temp.toString())
        f.close()
except Exception as e:
    print("예외 발생:", e)
finally:
    f.close()


import pickle
with open('./data/data.dat', 'rb') as f:
    result = pickle.load(f)
    for dto in result:
        print(dto.toString())



import zipfile
filelist = ["./test.txt"]
with zipfile.ZipFile('./test.zip', 'w', compression=zipfile.ZIP_BZIP2) as myzip:
    for temp in filelist:
        myzip.write(temp)
zipfile.ZipFile('./test.zip').extractall()

# 엑셀 파일 읽기
import openpyxl

# 엑셀 파일 포인터
wb = None

try:
    # 엑셀 파일에 포인터를 생성
    wb = openpyxl.load_workbook('./data/data/score.xlsx')
    # print(wb) # 경로 맞나 확인하고 주석처리 ㅎㅎ

    # sheet 가져오기
    ws = wb.active  # 현재 활성화된 sheet를 가져옴.
    # ws = wb.get_sheet_by_name("sheet이름")

    # 행단위 접근 - 각 행을 튜플로 접근
    # 읽어오는 개념이라 못고치도록 주는 것 ,,,,,
    for row in ws.rows:
        print(row)
        # 각 행의 인덱스
        print(row[0].value)
        print(row[0].row)

except Exception as e:
    print(e)

finally:
    if wb != None:
        wb.close()




# 엑셀 파일 읽기
import openpyxl
# 엑셀 파일 포인터
wb = None
try:
    # 엑셀 파일에 포인터를 생성
    wb = openpyxl.load_workbook('./data/data/score.xlsx')
    ws = wb.active  # 현재 활성화된 sheet를 가져옴.
    for row in ws.rows:

        # 1행 5열의 합계라고 설정
        if row[0].row == 1:
            ws.cell(row=row[0].row, column=5).value = "합계"
            continue

        # 합계 구하기
        total = row[1].value + row[2].value + row[3].value
        ws.cell(row=row[0].row, column=5).value = total

    # 파일에 기록
    wb.save("./data/score2.xlsx")
except Exception as e:
    print(e)

finally:
    if wb != None:
        wb.close()


# 데이터베이스 연동
###MYSQL접속
#mysql 접속
import pymysql

con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1025', db='user00', charset='utf8')

print(con)

con.close()