# 马士兵教育
# @Time : 2022/7/6 13:41
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project02

"""1、return语句的特点"""


def test1():
    print('执行test1函数')
    return
    print('hello')


# result = test1()
# print(result)

"""2、return 返回多个值"""


def test2(a):
    p = a ** 2
    l = a ** 3
    return p, l


def test3(a):
    p = a ** 2
    l = a ** 3
    return [p, l]


# r1, r2 =test2(9)
# result = test2(9)
# print(type(result))
# print(r1, r2)
r1, r2 = test3(9)
result = test3(9)
print(type(result))
print(r1, r2)
