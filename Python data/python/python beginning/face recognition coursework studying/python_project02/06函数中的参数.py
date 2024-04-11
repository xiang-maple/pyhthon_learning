# 马士兵教育
# @Time : 2022/7/6 13:41
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project02

"""1、必要传参 """


def test1(start, end):
    """计算从开始到结束之间，所有数字的和，包括结束"""
    s = 0
    for i in range(start, end+1):
        s += i
    return s


# print(test1(1, 100))
"""2、关键字传参"""
# print(test1(end=10, start=1))
"""3、默认传参"""


def test2(start, end, init_value=0):
    """计算从开始到结束之间，所有数字的和，包括结束"""
    s = init_value
    for i in range(start, end+1):
        s += i
    return s


print(test2(1, 10, 10))
"""4、不定长传参"""

def test3(*numbers):
    print(type(numbers))
    for i in numbers:
        print(i)


def test4(**kws):
    print(type(kws))

    for k, v in kws.items():
        print(f'参数的名字{k},参数的值：{v}')


# test3(10, 20, 30)
test4(a=10, b=20, c=30)