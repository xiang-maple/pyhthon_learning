# 小枫
# @Time : 2024/3/18 10:44
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

__all__ = ['test2']


def test1(a, b):
    print(a+b)


def test2(a, b):
    print(a * b)


# when only in the  xiaoxiao file, the def can be used.
if __name__ == '__main__':
    # this is my test data

    test2(1, 3)
    print(test1(10, 10))