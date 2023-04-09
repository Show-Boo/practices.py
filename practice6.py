absent = [2,5] #결석
no_book = [7] #책이 없는 학생
for student in range(1,11): #1~10번까지
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}이는 교무실로.".format(student))
        break
    print("{0}야, 책을 읽어봐".format(student))


# 출석번호가 1,2,3,4. 근데 앞에 100을 붙이기로 함. >> 101,102,103,104
student = [1,2,3,4,5]
student = [i + 100 for i in student]
print(student)

# 학생 이름을 길이로 변환
student = ["Iron man", "Thor", "I am groot"]
student = [len(a) for a in student]
print(student)

# 학생 이름을 대문자로 변환
student = ["Iron man", "Thor", "I am groot"]
student = [i.upper() for i in student]
print(student)




# 퀴즈 5
from random import *
passenger = 0 #총 탑승 승객 수
for a in range(1,51): #1~50 승객 수
    time = randrange(5,51) #5분~ 50분 소요 시간
    if 5 <= time <= 15: #5~15분 이내의 손님, 탑승 승객 수 증가 처리해야.
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(a, time))
        passenger += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(a, time))

print("총 탑승 승객 : {0}분".format(passenger))