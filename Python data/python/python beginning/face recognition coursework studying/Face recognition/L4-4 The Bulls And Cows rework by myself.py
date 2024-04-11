# 小枫
# @Time : 2024/3/16 10:39
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

import random  # produce the random number

print('Welcome to play Bulls And Cows')
print('Now, I would like to introduce the rules of the game to you')
print('Rule 1: The system will produce a random number from 1 to 10')
print('Rule 2: you can guess a number between them three times at best. When your guessed is right, the game over.')
print('Rule 3: the player is able to restart the game if you fail')
print('Now, if you want to begin the game, please enter yes or y, otherwise enter not or n')

i = 0  # the times of playing
while True:
    number = random.randint(1, 10)  # produce a number from 1 to 10
    order = input('please enter whether the game begin or not')
    if order == 'y' or 'yes':
        i += 1
        for j in range(1, 4):  # for loop is allowed to circulate 3 times at best
            my_number = int(input('please enter the number you guessed'))
            if my_number == number:
                print(f'Congratulations! your number {my_number} is right')
                break  # brea is used to over the loop such as for and while
            elif my_number < number:
                print(f'your number is less than the random number, you have {3-j} times to try again')
            else:
                print(f'your number is more than the random number, you have {3-j} times to try again')
    elif order == 'n' or "not":
        break

print('GAME OVER! Thank you for playing')
print(f'your game times is {i}')
