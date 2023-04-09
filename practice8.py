def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", age = 20, main_lang = "파이썬")
profile(main_lang = "자바", age = 25, name = "김태호")



# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()


profile("유재석", 20, "파이썬", "자바", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "코틀린", "스위프트")



# 지역변수와 전역변수
gun = 10
def checkpoint(soldiers): #경계근무
    global gun # 전역 공간에 있는 gun을 사용하겠다.
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) #2명이 근무 나감
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))



#퀴즈 6
def st_weight(height, gender):
    if gender == '남자':
        return height * height * 22
    else:
        return height * height * 21


height = 175
gender = "남자"
weight = round(st_weight(height/100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))