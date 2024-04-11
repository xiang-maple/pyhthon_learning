# 马士兵教育
# @Time : 2022/7/6 13:41
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project02

"""1、局部变量和全局变量"""


def test1(a):
    b = 100
    print(str1)
    return a + b


str1 = 'abbcefg'

# print(test1(10))
# print(a)
# print(b)

"""2、在函数中修改全局变量"""
num = 20  # 全局变量


def test2():
    global num  # 标识这个函数内部不是定义一个局部变量，而是修改全局变量
    num = 10
    print(f"当前函数的局部变量是：{num}")


test2()
print(num)
