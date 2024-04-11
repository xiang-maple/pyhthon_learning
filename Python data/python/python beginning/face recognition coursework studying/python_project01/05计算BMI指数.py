# 马士兵教育
# @Time : 2022/6/6 13:18
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project01
""" 1、Python的输入（身高和体重） """
h = input('请输入身高：单位是米')

w = input('请输入体重： 单位是千克')

# input函数，返回的所有数据都是字符串类型

h = float(h)
w = int(w)
# print(h)
# print(w)
# print(type(h))
# print(type(w))

""" 2、 Python的运算 """

'''一、 算数运算符'''
print(4 ** 0.5)
'''二、 赋值运算符 '''
a = 100
b, c, d = 10, 20, 30
e = f = 1000
''' 三、复合赋值运算符 '''

'''
1. 先算复合赋值运算符右侧的表达式
2. 再算复合赋值运算的算数运算
3. 最后算赋值运算
'''

# a += 10
a += 10 + 5
print(a)

""" 3、 Python的输出  """
name = '肖斌'  # 姓名
age = 40  # 年龄
my_id = 5  # 编号
''' 一 、 格式化输出符号 % '''
# print('我的年龄是:%d, 我的姓名是:%s' % (age, name))
# print('我的编号是: %04d' % my_id)
''' 二、 第二种格式化输出 f + {变量+ 表达式}  '''
# print(f'我的年龄:{age+1}, 我的姓名是：{name}')
''' 三 、 了解一下print的结束符 end '''
# print('abc', end='~')
# print(123, end='~')
# print('efg')  # \n 换行符
"""计算BMI指数"""
bmi = w / h ** 2
print(bmi)
# 只要保留小数点后面一位
print('我的BMI体质指数是: %.2f' % bmi)