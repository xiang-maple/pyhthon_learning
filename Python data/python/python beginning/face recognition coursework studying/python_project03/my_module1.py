# 马士兵教育
# @Time : 2022/7/20 14:30
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project03
__all__ = ['test1']


def test1(a, b):
    print(a + b)


def test2(a, b):
    print(a * b)


# 只在当前文件中调用该函数才会执行，其他导入的文件内不符合该条件，则不执行test1函数调用
if __name__ == '__main__':
    # 这是我们测试代码
    test1(10, 10)