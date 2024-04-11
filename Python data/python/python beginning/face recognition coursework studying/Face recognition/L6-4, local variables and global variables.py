# 小枫
# @Time : 2024/3/16 20:23
# @Author : 小贤
# @Version :3.11.4
# @IDE : PyCharm
# @Project : python

"""1. local variables and global"""


def tes1(a):
    b = 100  # (3)
    print(str12)
    return a + b  # I           have not understood the variables sry!


str12 = 'acfun'  # (1)but the global value cannot leave the function
"""2. modify the local variables in function"""
print(tes1(10))  # (2)
""" note the sequence the def, if print(test1(10)) 
is above the define of str12, So the variable is out of def"""

num = 20  # modify the  global argument


def tes2():
    global num  # sign the num is global, so the function is to modify the global instead of local
    num = 90
    print(f'the local variable is: {num}')


"""so the local variable must set in the frame of work
    and global variable must before the argument pass out"""

tes2()
print(num)  # even we leave the  function, num still be modified
