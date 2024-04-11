# 马士兵教育
# @Time : 2022/6/21 13:11
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project01

"""
年龄判断案例：
0 ~ 18 是 未成年
18 ~ 60 是 打工人
60以上 是老年人
"""

age = int(input('请输入你的年龄：'))

if age < 18:
    print(f"你的年龄是{age}, 未成年")
# elif age>=18 and age < 60:
elif 18 <= age < 60:
    print(f"你的年龄是{age}, 打工人")
else:
    print(f"你的年龄是{age}, 老年人")
