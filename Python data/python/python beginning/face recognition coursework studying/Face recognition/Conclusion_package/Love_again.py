# 小枫
# @Time : 2024/4/10 16:04
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : infer.py


import random
def loves(a,b):
    print(f"how love I am {a} to her, and {b} she to me")
def whet(a):
    rand = random.randint(0,9)
    your_number = random.randint(0,9)
    if your_number + a == rand:
        print("How will I quit her")
    else:
        print("I should persist to do it")
