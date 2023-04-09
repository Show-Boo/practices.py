print(abs(-5))

#floor 함수 : 내림
#ceil 함수 : 올림
#sqrt 함수 : 제곱근

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의 값 생성
print(random()*10) #0.0 ~ 10.0 미만의 임의 값 생성
print(int(random())) #0 ~ 10 미만
print(int(random() * 10) + 1) #1 ~ 10 이하

#로또
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)

print(randrange(1,46)) #1 ~ 46 미만의 임의 값 생성하라.

#퀴즈#2 내 풀이
from random import *
a = int(random()*28)+3
print("오프라인 스터디 모임 날짜는 매월", a ,"일로 설정되었습니다.") 
#퀴즈#2 정답
from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 설정되었습니다.")