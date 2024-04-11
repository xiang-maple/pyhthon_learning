# 马士兵教育
# @Time : 2022/7/14 16:06
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project02

import random

lst = ['石头', '剪刀', '布']


def start_window():  # 游戏开始界面
    print('*************************')
    print('--------1.进入游戏--------')
    print('--------0.退出游戏--------')
    print('*************************')


def start_game():  # 进入猜拳界面
    print('请进行猜拳：')
    print('*************************')
    print('--------1.石   头--------')
    print('--------2.剪   刀--------')
    print('--------3.  布  ---------')
    print('--------0.退出游戏--------')
    print('*************************')


def print_result(m, n, result):
    """
    打印游戏的结果
    :param m: 用户输入的
    :param n: 电脑随机生成的
    :param result: 结果字符串
    :return:
    """
    my_choice = lst[m - 1]  # 将输入的数字转换成文字（1.石头 2.剪刀 3.布）
    com_choice = lst[n - 1]  # 将输入的数字转换成文字（1.石头 2.剪刀 3.布）
    print(f"你的选择是:{my_choice}")
    print(f"电脑的选择是:{com_choice}")
    print(result)


print("欢迎来到我的猜拳游戏！")
while True:
    start_window()  # 进入欢迎界面
    i = int(input("请输入你的选择："))  # 进入游戏或者退出游戏
    if i == 1:  # 用户开始游戏
        start_game()
        m = int(input("请输入你的选择："))
        if m == 0:
            break  # 退出游戏界面
        if m < 1 or m > 3:
            print("输入的数值不合法")
            break
        n = random.randint(1, 3)  # 电脑随机生成的整数
        if m == n:
            print_result(m, n, "平局")
        elif m - n == 1 or m - n == -2:
            print_result(m, n, '对不起，你输了！')
        else:
            print_result(m, n, '恭喜你， 你赢了！')
    elif i == 0:
        print("退出游戏")
        break
