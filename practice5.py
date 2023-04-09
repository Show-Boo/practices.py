#if문

# weather = input("오늘 날씨는? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")


# temp = int(input("오늘 기온은 어때요? "))
# if 30 <= temp :
#     print("너무 더움")
# elif 10<= temp and temp <30:
#     print("적당")
# elif 0<= temp and temp<10 :
#     print("겉옷 챙겨")
# else:
#     print("나가지마")


#for문

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

for waiting_no in range(1, 5): # 1,2,3,4 (1부터 5 전까지)
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))


# while문
# customer = "토르"
# a = 5
# while a >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, a))
#     a -=1
#     if a == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# a = 1
# while True:
#     print("{0}, 커피가 준비되었습니다.".format(customer, a))
#     a += 1

customer = "토르"
person = "Unknown"

while person != customer: 
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
    print("여기 있습니다. 감사합니다.")









