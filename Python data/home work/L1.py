# 小枫
# @Time : 2024/4/1 18:01
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : infer.py
# 1.
# print("莫道谗言如浪深，")
# print(f"莫言迁客似沙沉。")
# print("%s" % "千淘万漉虽辛苦，")
# print("吹尽狂沙始到金。")
# 2.
# while True:
#     a = int(input("input a number"))
#     if a > 68:
#         print("the answer is high")
#     elif a<68:
#         print("the answer is low")
#     else:
#         print("answer is right")
#         break
# 3.
# while True:
#     b = input("please input administration")
#     if b == "administration":
#         print("admin")
#         break
#     else:
#         print("wrong")
# 4.
# while True:
#     c = int(input("please input a number"))
#     if c%2 == 0:
#         print("number is even")
#     if c%2 == 1:
#         print("number is odd ")
#     if c == 10:
#         print("10 is special number,the game is over")
#         break
# 5.
# while True:
#     w = int(input("your weight in kilograms\n"))
#     h = float(input("your height in meters\n"))
#     BMI = w/h**2
#     if BMI < 18.5:
#         print("you are too thin")
#     elif BMI>=18.5 and BMI<25:
#         print(f"you are normal,BMI is {BMI}")
#     elif 25 <= BMI <=28:
#         print(f"you are heavy,BMI is {BMI}")
#     elif 28 < BMI <=32:
#         print(f"you are too heavy,BMI is {BMI}")
# 6.
# x=float(input("x number is "))
# y=float(input("x number is "))
# if x>0 and y>0:
#     print("in Quadrant 1")
# if x<0 and y>0:
#     print("in Quadrant 2")
# if x<0 and y<0:
#     print("in Quadrant 3")
# if x>0 and y<0:
#     print("in Quadrant 4")
# if x==0 and y==0:
#     print("in origin")
# elif x==0 or y==0:
#     print("in x axis or y axis")
# 7.
# ms_num = 0
# print("you have three times to do it ")
# while ms_num < 3:  # this cannot use == (process will complete)
#     ms_num += 1
#     ms = int(input("the months in number you input to distinguish which season it is belong\n"))
#     if 3<=ms<=5:
#         print(f"{ms} months beling to spring")
#     if 6<=ms<=8:
#         print(f"{ms} months beling to summer")
#     if 9<=ms<=11:
#         print(f"{ms} months beling to autumn")
#     if ms in (12, 1, 2):
#         print(f"{ms} months beling to winter")
# t = 0
# while t < 10:
#     t += 1
#     y = int(input("year\n"))
#     m = int(input("months\n"))
#     # 1、3、5、7、8、10、12 每月31天，4、6、9、11为30天。 二、2月正常为28天
#
#     if m in (1,3,5,7,8,10,12):
#         print(f"this month have 31 days")
#     if m in (4,6,9,11):
#         print(f"this month have 30 days")
#     if m == 2 and y%4==0 and y%100!=0:
#         print(f"this month have 29 days ")
#     elif m == 2:
#         print(f"this month have 28 days")
y = int(input("year\n"))
if y%4==0 and  y%100!=0:
    print(f"this year is leap year")
else:
    print("not leap year")

