'''
a,b,c = input('세 수를 입력하시오. ').split()
a = int(a)
b = int(b)
c = int(c)

print(a+b+c)
'''


#과제 1 '업 다운 게임'
# from random import *
# number = int(randrange(0,101))

# while True: 
#     answer = int(input('숫자를 입력하시오 : ')) 
#     if number < answer:
#         print('다운')
#     elif number > answer:
#         print('업')        
#     else:
#         print('정답')
#         break



# #과제 2
# from random import *
# RSP = ['가위', '바위', '보']

# while True:
#     computer = choice(RSP) # 컴퓨터 픽
#     answer = input('가위 바위 보 중에 입력\n 종료하려면 ''게임종료''를 입력하시오 ')
    
#     if answer ==  '가위':
#         if computer == '가위':
#             print('컴퓨터는 {0}을 냈습니다'.format(computer))
#             print('무승부')
#         elif computer == '바위':
#             print('컴퓨터는 {0}을 냈습니다'.format(computer))
#             print('패배')
#         else:
#             print('컴퓨터는 {0}을 냈습니다'.format(computer))
#             print('승리')
#     elif answer == '바위':
#         if computer == '가위':
#             print('컴퓨터는 {0}을 냈습니다'.format(computer))
#             print('승리')
#         elif computer == '바위':
#             print('컴퓨터는 {0}을 냈습니다'.format(computer))
#             print('무승부')
#         else:
#             print('컴퓨터는 {0}을 냈습니다'.format(computer))
#             print('패배')
#     elif answer == '보':
#         if computer == '가위':
#             print('컴퓨터는 {0}을 냈습니다'.format(computer))
#             print('패배')
#         elif computer == '바위':
#             print('컴퓨터는 {0}을 냈습니다'.format(computer))
#             print('승리')
#         else:
#             print('컴퓨터는 {0}을 냈습니다'.format(computer))
#             print('무승부')
#     else:
#         break



# for i in range(3):
#     for j in range(3):
#         print("ㅁ", end = '')
#     print()


# from random import *
# member = 0
# for number in range (1,51):
#     time = randint(5,51)
#     if time < 15:
#         print("[o]{0}번째 손님 (소요시간 : {1}분)".format(number,time))
#         member = member + 1
#     else:
#         print("[ ]{0}번째 손님 (소요시간 : {1}분)".format(number,time))

# print(member,"명")




answer = int(input())