# 小枫
# @Time : 2024/3/15 20:54
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python studying pro
# import random  # specialized module for random product
# from random import randint
# import random as suiji
# from random import randint as talented
from random import *

print('welcome to the Bulls and Cows')
print('rule 1: the system will produce a random number between 1 and 10 every time')
print('rule 2: every time of game should be guess three times')
print('rule 3: if you want to enter the game and continue to do it, please input: yes or y')

i = 0  # the times of playing game
while True:
    number = randint(1, 10)  # produce a random from 1 ~ 10
    order = input('please enter whether begin the game or not')
    if order == 'yes' or order == 'y':
        i += 1
        for j in range(1, 4):  # for loop is allowed to circulate for three times at best
            my_num = int(input('please enter the number you guess'))

            if my_num == number:
                print(f'Congratulation you guessed the number:{my_num}')
                break
            elif my_num > number:
                print(f'Sorry for you guess big, you have {3-j} chances to guess again')

            else:
                print(f'Sorry for you guess small, you have {3-j} chances to guess again')

    elif order == 'no' or order == 'n':
        break

print('GAME OVER! Thanks For Playing')
