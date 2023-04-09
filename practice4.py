#사전
cabinet = {3: "김부성", 10 : "김태호"}
print(cabinet)

#튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"
print(name,age,hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name,age,hobby)



#set
#중복 x, 순서 x
s = {1,2,3,3,3}
print(s)
java = {"김부성", "유재석", "양세형"}
python = set(["김부성", "김종국"])

#교집합 (java와 python 모두 가능)
print(java & python)
print(java.intersection(python))

#합집합 (java or python)
print(java | python)
print(java.union(python))

#차집합 (java는 할 수 있지만 python은 할 줄 모름)
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 까먹음.
java.remove("유재석")
print(java)




#자료구조의 변경
#커피숍
menu = {"커피","주스","우유"}
print(menu, type(menu))

menu = list(menu)
print(menu,type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))




#퀴즈 4

# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))


from random import *
users = range(1, 21) #1부터 20까지 숫자 생성
users = list(users)
print(users, type(users))
shuffle(users)

winners = sample(users, 4) #4명 중에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")