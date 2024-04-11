# 小枫
# @Time : 2024/4/10 12:35
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : infer.py
# """necessary parameters"""
# """attain the sum of start to end"""
# def tes1(start, end):
#     s = 0
#     for i in range(start,end+1):
#         s+= i
#     return s
# print(tes1(1, 10))
#
# """keyword parameter"""
# print(tes1(end=12,start=10))
#
# """default parameter"""
# def tes2 (start, end, init_value=0):
#     s = init_value
#     for i in range(start,end+1):
#         s+= i
#     return s
# print(tes2(1,2,1))
# print(tes2(1,2,))
#
# """random length parameter"""
# """general"""
# def tes3(*numbers):
#     i = 0
#     print(type(numbers))
#     for s in numbers:
#         i += s
#     return print(f"the sum of numbers is {i}")
#
# input1 = int(input("please enter your name\n"))
# input2 = int(input("please enter your name\n"))
# input3 = int(input("please enter your name\n"))
#
# tes3(input1,input2,input3)

"""keyword"""
def tes4(**mnum):
    print(type(mnum))
    s =0
    for k,v in mnum.items():

        s += v

        print(f"your key is{k}, you value is {v}")
    return s
tes4(a=1,b=3,c=5)