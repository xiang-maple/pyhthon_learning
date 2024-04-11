# 小枫
# @Time : 2024/3/27 13:39
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : Python data

# """---L1-1 Welcome to the python,__________________ how to use print---"""
# print("Hello world")
# # format output
# # first way (this way's outcome both are str)
# pw = 54321
# print(f'your password is: {pw}')
# # second way (f, d, s)
# fn = 1.635984768934789
# print('the rounded off to 2 decimal place is %.2f' % fn)
# name = "jiangxin"
# print("my name is %s" % name)
# dint = 150000
# print("my dint is %02d" % dint)
#
# """---L2-1 variables and operators---"""
# # basic variables form
# print('choose the alphabet from a to g, to show its data class')
# print('if you want to over the game, please input: over')
#
#
# # the type of variables
# a = 123  # int
# b = 'name'  # str
# c = 3.1415926535  # float
# d = [1, 2, 3, 4]  # list
# e = {1, 2, 3, 3}  # set
# f = (1, 2, 3, 4)  # tuple
# g = {'a1': "a", "a2": 3}  # dictionary
# ses = [a,b,c,d,e,f,g]
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
#
# #  operator
# # arithmatic operator
# # order: ()>**>* / // %(maybe their order is sequence)>+ -
# a = 1
# b = 2
# c = 10
# d = 3.1
# print(a+b)
# print(a-b)
# print(a*b)
# print(c**b)
# print(c/b)
# print(c//d)
# e = c%d
# print(e)
# print("anser %.1f" %e)
# print(130//10%3)  # the answer is 1, not 130
#
# # assignment operator
# abc =1
# print(abc)
#
# # compound assignment operation
# a += b
# # a -= b  # remmember annotation to do the print
# b *= c
# c **= b
# # b /= d
# # c //= d
# # c %= d
# print(a)
# print(b)
# print(c)
#
# # comparison operator
# an = int(input("an number"))
# bn = int(input("bn number"))
# if an < bn:
#     print("bn win")
# elif an > bn:
#     print("an win")
# elif an == bn:
#     print("no win")
# cn = float(input('cn answer'))
# dn = float(input('dn answer'))
# if cn != dn:
#     print(" we can't come together")
# en = int(input("en int"))
# fn = int(input('fn int'))
# if en >= fn:
#     print("en cool")
# else:
#     print("fn cool")
#
# # logical operator
# if an > bn or an < bn:
#     print("we can't come together")
# if an > bn and en <= fn:
#     print('complex answer')
# if not an > bn and not an < bn:
#     print("we can come together")
#
#
#
"""
pay attention to the way below. When I review the loop and data base, I should try it again
"""

# a = 123  # int
# b = 'name'  # str
# c = 3.1415926535  # float
# d = [1, 2, 3, 4]  # list
# e = {1, 2, 3, 3}  # set
# f = (1, 2, 3, 4)  # tuple
# g = {'a1': "a", "a2": 3}  # dictionary
# ses = [a, b, c, d, e, f, g]
# while True:
#     ip = input('input your choice')
#     if ip in ses:  # int
#         print(type(ip))
#
#
#     elif ip not in ses:
#         print("you answer is not effective")
#
#     elif ip == 'over':
#         print('game is over')
#         break
# #
# """---L3-1 Loop statemrnt and Conditional statement---"""
# """--Loop--"""
# """While loop"""
#
#  first type of while loop (True loop)
# # break using
# while True:
#     var = int(input("number you input"))
#     if var >= 2:
#         print("I cool")
#         break
#     elif var<=1:
#         print('you are right')
# # continue using
# while True:
#     var = int(input("number you input"))
#     if var >= 2:
#         print("I cool")
#         continue
#     print('you died')
#     break

# Second type of while condition loop
# i = 0
# while i<=10:
#     i += 1
#     c = int(input("number"))
#     if c <= 101:
#         continue
#      break
# i = 0f
# while i<=10:
#     i += 1
#     c = int(input("number"))
#     if c <= 101:
#         """
#         the usage of break is respond the while instead of if
#         """
#         break

# """for loop"""
# j = 0
# an = 0
# h = 0
# for j in range(1,11):
#     h += 1
#     an += h
#     print(an)
# print(an)

"""--condition statement--"""
"""
if and elif can be more , but else can't be right
"""
# while True:
#     num = int(input("number"))
#     if num == 0:
#         break
#     if num > 0 and num <= 10:
#             print("prime")
#     elif num > 10 and num <= 1000:
#         print("middle")
#     else:
#         print("senior")
"""---THE GAME BULLS AND COWS---"""
# import random  # produce the random number
#
# print('Welcome to play Bulls And Cows')
# print('Now, I would like to introduce the rules of the game to you')
# print('Rule 1: The system will produce a random number from 1 to 10')
# print('Rule 2: you can guess a number between them three times at best. When your guessed is right, the game over.')
# print('Rule 3: the player is able to restart the game if you fail')
# print('Now, if you want to begin the game, please enter yes or y, otherwise enter not or n')
#
# i = 0
# number = random.randint(1,10)
# while True:
#     gb = input("choose whether enter nor not ")
#     if gb == "y" or gb == "yes":
#         i += 1
#         for j in range (1,4):
#             num = int(input("please input your number from 1 to 10, if you input other number the game will over"))
#             if num > 10 or num<= 0:
#                 break
#             elif num < number:
#                 print(f"your number is lower than the random, FAIL, you have {3-j} chance to guess the number")
#             elif num > number:
#                 print(f"your number is higher than the random, FAIL, you have {3-j} chance to guess the number")
#             elif num == number:
#                 print("your number is equal to the random, Win")
#                 break
#
#     elif gb == 'n' or gb == "not":
#         break
# print("game over")
# print(f"your game time is {i}")
# """---data base---"""
# """--list--"""
#
# # format
# lst = [1,2,34,65,1.5, (1,2), {1,2}, {"a":1, "b":3}, True, "cool",]
# print(lst)
# # check it
# print(lst[0:10])
# print(lst[-10:-1])
# print(lst[-1])
# print(lst.index(1.5))
# print(len(lst))
# if 10 in lst:
#     print("yes")
# else:
#     print("not")
# for i in lst:
#     print(i)
# j = 0
# while j <= 10:
#     print(lst[j-1])
#     j += 1
# # modify the lst
# lst.append(10)
# lst.insert(0,19)
# print(lst)
# lst.pop(1)
# lst.remove(34)
# print(lst)
# lst[1] = "xiaoxiao"
# print(lst)
#
# """--tuple--"""
# # creat
# tup = (1,2,True,4.5,[1,2],1.23)
# false_tup = (1)
# right_tup = (1,)
# print(right_tup)
# # check
# print(tup[0])
# print(tup[0:5])
# print(tup.index(2))
# if 1.23 in tup:
#     print("1.23 is in tup")
# else:
#     print("1.23 not in tup")
# ii = 0
# # while ii < len(tup):
# #
# #     print(tup[ii])
# #     ii += 1
# while ii < len(tup):
#
#     ii += 1
#     print(tup[ii-1])
# for kk in range(len(tup)):
#     print(tup[kk])
# print(len(tup))
# print(range(len(tup)))
#
#
# """--dictionary--"""
# # creat format
# dic = {"a":1, "b":"ad", "c":1.23, "d":[1,23]}
# print(dic)
# dic1 = {}
# # check
# print(dic["a"])
# # print(dic["f"])
# print(dic.get("f"))  # it's better to show the error show none instead of show error
#
# for k in dic.keys():
#     print(k)
# for v in dic.values():
#     print(v)
# for kk, vv in dic.items():
#
#     print(kk,"" ,":", vv)
# for al in dic.items():
#     print(al)
# if 1 in dic:
#     print("a in dic")
# else:
#     print("shir")
# if 'a' in dic:
#     print("a in dic")
# else:
#     print("shir")
# # modify
# dic["g"]=100
# dic['w']=1.2323
# del(dic["a"])
# print(dic)
# dic["b"]=213
# print(dic)
#
# """--set--"""
# st_wrong = {123,[],{},()} # this is wrong format
# st = {1,232,5,1.234}
# st2 ={}
#
# # check
# s = 0
# # while s <= len(set):
# #     s += 1
# #     print(set[s])  # no index so  we use for
# for s in st:
#     print(s)
# # modify
# st.add(123213)
# st.update([123,1.2323])
# print(st)
# st.remove(1)
# print(st)
# st.remove(232)  # how to remove a lot of data
# st.add(1243)
# print(st)
# """
# Conclusion      order/index      modify
# list            have             yes        (way)append insert pop remove
# tuple           have             not        (way)not
# dictionary      have             yes        (way)[""]=  del
# set             not have         yes        (way)add remove update
#
#
#
# """

# """---function---"""
# """--the function you create--"""
# __all__ = ["abs"]  # choose whether use it or not
# def abs(a):
#     if a >= 0:
#         return a
#     elif a < 0:
#         return -a
# # test data protect
# if __name__ == '__main__':
# # if __name__ == "__main__":
#     ty = abs(-9)
#     print(ty)
#
# """--parameter passing--"""
# """--First Necessary parameter passing--"""
# def nece(a,b,c):
#     s = a+b-c
#     return s
# num = nece(1,2,3)
# print(num)
# """--Second keyword parameter passing--"""
# num = nece(c=1,a=3,b=9)
# print(num)
#
# """--Third default parameter passing--"""
# def defat(a,b,init_value=0):
#     s = init_value
#     for i in range(1,11):
#         s += a
#         s -=b
#     return s
# wy = defat(3,2)
# print(f"my answer is {wy}")
#
# """--Fourth general random parameter passing--"""
# def rand(*nums):
#     print(type(nums))
#     for i in nums:
#         print(i)
# num1 = rand(1,23,56)
#
#
# """--Fifth keyword random parameter passing--"""
# def krand(**nums):
#     print(type(nums))
#     for k,v in nums.items():
#         print(k,v)
# num2 = krand(a=1,b=3,c=9)
# """---local variables and global variavles---"""
# aum = 10
# def sum(a):
#     aum =123
#     s = aum +a
#
#     return s
# # print(s)  # there is error
# print(sum(10))
# tum = 10
# print(sum(10))
# def sum(a):
#     aum =123
#     s = aum +a
#     global tum
#     tum += s
#     return s
# sum(10)
# print(tum)
# """---function import---"""
# """--first--"""
# import Conclusion_function_test
# print("the highest mark is 10")
# Conclusion_function_test.love(10,10)
# """--second--"""
# from Conclusion_function_test import love
# love(10,10)
# """--third--"""
# from Conclusion_function_test import *
# whe(2)
# # love()  # there is error
# """--fourth--"""
# import Conclusion_function_test as ct
# ct.love(10,10)
# """--fifth--"""
# from Conclusion_function_test import love as lv
# lv(10,10)

# """---moude---"""
# """--first--"""
# # import Conclusion_package.Love_again
# # import Conclusion_package.hello  # except the init.py other pyfile we should add their name to ues its function
# # Conclusion_package.Love_again.whet(2)
# # Conclusion_package.hello.Hello()
# #
# # """--second--"""
# # from Conclusion_package import hello
# # hello.Hello()
#
# """--third--"""
# from Conclusion_package import *
# #hello.Hello()  # error
# Love_again.whet(2)
#
# """--fourth--"""
# from Conclusion_package import Love_again as le
# le.whet(2)
#
# """--fifth--"""
#
# import Conclusion_package.Love_again as al
# al.whet(2)
