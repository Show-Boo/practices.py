#\n : 줄바꿈
from random import random


print("백문이 불여일견 백견이\n불여일타")

#저는 "나노 코딩" 입니다. 출력
print("저는 \"나노코딩\" 입니다.")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")


#예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#예) 생성된 비번 :  nav51!
url = "http://naver.com" 
a = url.replace("http://","") # 규칙 1
a = a[0:a.index(".")] # 규칙 2
password = a[0:3] + str(len(a)) + str(a.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))



# 리스트

#지하철 칸별로 10, 20, 30명
subway = [10,20,30]
print(subway)

subway = ["김부성", "김붐섬", "김병선"]
# 김붐섬씨는 몇 번째 칸에 타고 있나?
print(subway.index("김붐섬"))

#김븅진씨가 다음 정류장에서 탐.
subway.append("김븅진")
print(subway)

#김벽적씨를 김부성, 김붐섬 사이에 넣는다.
subway.insert(1, "김벽적")
print(subway)

# 지하철에 있는 사람 뒤에서부터 한 명씩 꺼냄
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

#정렬도 가능
a = [5,2,4,3,1]
a.sort()
print(a)

#순서 뒤집기
a.reverse()
print(a)

#모두 지우기
a.clear()
print(a)