# Data Visualization
#시각화 패키지
import matplotlib.pyplot as plt

#꺽은선 그래프
#그래프 그릴 영역
plt.figure()
#옵션을설정
plt.plot([100, 300, 200])
#출력
plt.show()

#옵션 변경
#데이터 생성
s1 = [74900, 79000, 78000, 79300]
s2 = [80010, 80200, 80100, 80200]

#그래프 크기 설정
plt.figure(figsize=(10,4))

#그래프 그리기
plt.plot(s1, label='02-07')
plt.plot(s1, label='02-08')

plt.grid()
plt.xlabel('index')
plt.ylabel('stock')

plt.title('plot graph')

plt.legend()
#그래프를 화면에 출력
plt.show()

# Data Visualization
#시각화 패키지
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
import matplotlib
#csv를 읽기 위한 패키지
import csv

#윈도우의 경우
if platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)


#음수 출력
matplotlib.rcParams['axes.unicode_minus'] = False

#한글 출력

#데이터 생성
s1 = [74900, 79000, 78000, 79300]
s2 = [80010, 80200, 80100, 80200]

#그래프 크기 설정
plt.figure(figsize=(10,4))

#그래프 그리기
plt.plot(s1, label='02-07')
plt.plot(s1, label='02-08')

plt.grid()

plt.xlabel('인덱스')
plt.ylabel('주가')

plt.title('꺽은선 그래프')

plt.legend()

#그래프를 화면에 출력
plt.show()

#csv 파일을 읽어서 꺽은선 그래프로 출력하기
#데이터 읽기
f = open('./data/mk.csv')
data = csv.reader(f)

#첫번째 줄은 열의 제목이므로 제외
next(data)

for row in data:
    print(row)




#numpy
#list와의 작업 시간 비교
import numpy as np
import datetime

#list 생성 - 1부터 100만....
li = list(range(0,1000000,1))

#현재 시간을 가져오기
start = datetime.datetime.now()
print("리스트 작업 시작 시간:", start)

#모든 데이터에 10을 곱해서 저장
for i in li:
    i*10

end = datetime.datetime.now()
print("리스트 작업 종료 시간:", end)

ar=np.arange(0,1000000,1)

#현재 시간을 가져오기
start = datetime.datetime.now()
print("배열 작업 시작 시간:", start)

ar*10

end = datetime.datetime.now()
print("배열 작업 종료 시간:", end)


#ndarray 의 생성과 정보 확인 - 실제 생성은 학습할 때만 이렇게 함
import numpy as np
#일차원 배열 생성
ar = np.array([1,2,3])
#ar의 자료형 확인
print(type(ar))
#ar의 요소의 자료형 확인
print(ar.dtype)

print(ar.ndim) #1차원
print(ar.shape) #1차원인데 데이터 3개


#numpy의 함수를 이용한 ndarray생성
import numpy as np

ar = np.arange(10)
print(ar)
#마지막 데이터를 포함
ar=np.linspace(0,1,6)
print(ar)
print()
#마지막 데이터를 포함시키지 않음
ar=np.linspace(0,1,6, endpoint=False)
print(ar)
print()


#특수 행렬
import numpy as np
#1로 10을 채운 배열을 생성
ar1 = np.ones(10)
print(ar1)

#1로 채워진 5*5 배열 생성
ar2 = np.ones((5,5))
print(ar2)

#2*2 정방 행렬을 만들고 대각선 방향으로 1을 채운 행렬 생성
ar3 = np.eye(2)
print(ar3)


#요소의 데이터 타입을 변경
import numpy as np
#type 설정해서 생성
ar =np.array([1,2,3], dtype=np.int32)
print(ar.dtype)
#type을 float32로 변경
ar=ar.astype(np.float32)
print(ar.dtype)

#행렬의 구조 변경 -reshape,flattern
import numpy as np
#1차원 배열 생성
ar = np.arange(10)
print(ar)
#2차원 배열로 변환
br=ar.reshape(2,5)
print(br)
#2차원 배열을 1차원 배열로 변환
print(br.reshape(-1))
print(br.flatten())

#1차원 배열을 생성
ar = np.arange(20)
print(ar.reshape(2,5,2))

#1차원 배열을 3차원으로 변환
print(ar.reshape(2,5,2))
#마지막 차원의 개수는 -1로 설정하면 알아서 분할해서 생성해 줌
print(ar.reshape(2,5,-1))