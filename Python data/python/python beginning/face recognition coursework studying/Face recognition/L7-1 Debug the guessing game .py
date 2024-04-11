# 小枫
# @Time : 2024/3/16 21:43
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

import random  # 1

lst = ['rock', "scissors", 'paper']  # 2


def start_window():  # gaming beginning 3
    print('------1.game start------')
    print('------0.game out--------')


def start_game():  # enter the game screen 4
    print('please guess')
    print("---1.rock---")
    print('---2.scissors---')
    print('---3.paper---')
    print('---0.out---')


def print_result(t, p, result):  # 5
    my_choice = lst[t - 1]
    com_choice = lst[p - 1]
    print(f'my choice is {my_choice}')
    print(f'com_choice is {com_choice}')
    print(result)

print('welcome to my game')


while True:
    start_window()
    i = int(input('please input your choice\n'))  # whether enter the game or not 6
    if i == 1:  # the user start the ga!me  # 7
        start_game()  # 8
        m = int(input("enter your choice\n"))  # 8
        if m == 0:
            break  # game out
        if m < 1 or m > 3:
            print('invalid choice')
            break
        n = random.randint(1, 3)  # compute produce the random int
        if m == n:
            print_result(m, n, "no win")
        elif m - n == 1 or m - n == -2:
            print_result(m, n, "fail")
        else:
            print_result(m, n, "win")
    elif i == 0:
        print('game over')
        break
