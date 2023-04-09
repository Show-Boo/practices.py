# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# import pickle
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))



#퀴즈 7
# report_file = open("report.txt", "w", encoding = "utf8")


# for date in range(1,51):
#     print("- {0} 주차 주간보고 -".format(date), file = report_file)
#     print("부서 : ", file = report_file)
#     print("이름 : ", file = report_file)
#     print("업무 요약 : ", file = report_file)
# report_file.close()
#ㅡㅡㅡㅡ 내정답 ㅡㅡㅡㅡ

'''
for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding = "utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")        
'''