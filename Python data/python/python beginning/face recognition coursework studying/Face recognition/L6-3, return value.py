# 小枫
# @Time : 2024/3/16 20:03
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

"""1.return sentence characters"""

def none_return():
    print("1")
    print("with out return or return withour anything ")
    return 0  # if I not use value or not return , it will return nothing
none_return()  # this is only process the function
ses = none_return()  # this we get return as ses
print(ses)  # this get return
def tes1():
    print(1)
    return 10  # if we use return, the code behind the return would not be acted.
    print("hello")


result = tes1()
print(result)

"""2. return many values"""


def tes3(a):
    s = a ** 2
    t = a ** 3
    return [s, t]

def tes2(a):
    r1 = a*2
    r2 = a*3
    return r1,r2

result = tes2(9)

print(type(result))

r1,r2 = tes2(9)
print(r1, r2)

r1, r2 = tes3(9)  # test3(9) is the list
result = tes3(9)

print(type(result))
print(result)
# print(test3(9))
# print([r1, r2])
