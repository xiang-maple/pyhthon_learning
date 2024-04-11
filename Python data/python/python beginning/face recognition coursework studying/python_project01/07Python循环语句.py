# 马士兵教育
# @Time : 2022/6/21 13:50
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project01

"""
计算从1 ~ 100所有 偶数的和
"""

# 第一种：采用while循环

# i = 1
# result = 0
# while i <= 100:
#     if i % 2 == 0:
#         result += i
#     i += 1
#
# print(result)

# 第二种：采用while循环 + break

# while True:  # 死循环
#     if i > 100:
#         break  # 终止循环
#     if i % 2 == 0:
#         result += i
#     i += 1
#
# print(result)

# 第三种： 采用while循环 + continue
# i = 0
# result = 0
# while i <= 100:
#     i += 1  # 变量i 从1开始依次加1 来变化。
#     if i % 2 == 1:  # 是奇数
#         continue
#     result += i  # 累加
#
# print(result)

# 第四种： 采用for循环
result = 0
for i in range(1, 101):   # 从1 ~ 100
    if i % 2 == 0:
        result += i

print(result)