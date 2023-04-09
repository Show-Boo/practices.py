boo = "010606-1234567"

print("성별 : " + boo[7])
print("연 : " + boo[0:2]) # 0번째부터 2번째 직전까지 가져온다
print ("월 : " + boo[2:4])
print("일 : " + boo[4:6])

print("생년월일 : " + boo[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + boo[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + boo[-7:]) # 맨 뒤에서 7번째부터 끝까지



#문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 파이썬의 첫번째가 대문자인가요?
print(len(python)) #파이썬의 글자 길이
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) #(거짓(없음))

print(python.count("n"))


#문자열 포맷
#방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬") # s는 문자열을 넣겠다는 소리.
print("Apple은 %c로 시작해요." % "A") # c는 한 글자만 받겠다는 소리.
# %s
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아한다." % ("파란", "빨간"))

#방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아한다.".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아한다.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아한다.".format("파란","빨간"))

#방법 3
print("나는 {age}살이고, {color}색을 좋아해.".format(age = 20, color = "빨간"))

#방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이고, {color}색을 좋아해.")