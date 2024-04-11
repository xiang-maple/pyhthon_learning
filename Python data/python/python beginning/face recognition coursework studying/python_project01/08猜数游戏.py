# 马士兵教育
# @Time : 2022/6/21 14:56
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project01
import random  # 专门产生随机数的模块

print("-" * 50)
print("欢迎来到 老肖 的《猜数游戏》")
print("规则一：系统每次会自动生成一个1~10之间的随机数")
print("规则二：每次游戏最多只能猜三次")
print("规则三：进入游戏或者继续玩，输入：yes或者y")
print("规则三：离开游戏，输入：no或者n")
print("-" * 50)

i = 0  # 玩游戏的次数
while True:
    number = random.randint(1, 10)  # 产生一个1 ~ 10 之间的随机数
    order = input('请输入是否开始游戏：')
    if order == 'yes' or order == 'y':
        i += 1
        for j in range(1, 4):  # for循环中最多允许猜三次
            my_num = int(input('请输入所猜的数字：'))

            if my_num == number:
                print(f'恭喜你! 猜中了，就是数字:{my_num}')
                break
            elif my_num > number:
                print(f'你猜的太大了，还剩下{3-j}次')
            else:
                print(f'你猜的太小了，还剩下{3 - j}次')
    elif order == 'no' or order == 'n':
        break

print("谢谢！ GAME OVER")
