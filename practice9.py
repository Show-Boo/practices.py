import sys

print("김", "부", "성", sep = " vs ", end = "?")
print("김부성", "성부김", file = sys.stdout)
print("김부성", "성부김", file = sys.stderr)

#시험 성적
scores = {"수학":0, '영어':50, '코딩':100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8) , str(score).rjust(4),sep = ":") #오른쪽 정렬



# 은행 대기 순번표
#001, 002, 003, ...
for num in range (1,21):
    print("대기번호 : " + str(num).zfill(3)) #zfill : 0 채우기


# answer = input("아무 값이나 입력하시오. : ")
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")



# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))
# 양수일 때 +로 표시, 음수일 때 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
#왼쪽 정렬하고, 빈칸으로 _ 채움
print("{0:_<+10}".format(500))
# 3자리마다 콤마를 찍어주기
print("{0:,}".format(1000000000000))
# 3자리마다 콤마를 찍고, 부호 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니 빈 자리에 ^로 채우기
print("{0:^<+30,}".format(10000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수까지만 표시
print("{0:.2f}".format(5/3))