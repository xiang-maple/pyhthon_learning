# 小枫
# @Time : 2024/3/15 19:55
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python studying pro

"""
the case of age judging
0 ~ 18 are underage
18 ~60 are worker
above 60  are elder
"""

age = int(input('please enter your age: '))

if age < 18:
    print(f'your age is {age}, underage')
elif 18 <= age <= 60:  # pay attention to the usage of age >== 18, age <== 60 is not best.
    print(f'your age is {age}, worker')
else:
    print(f'your age is {age}, elder')  # what is the retracted!!!!!!!!!

print("Now you can comment how you are hard, the number range from 1 to 10")

hard = 8
normal = 5
no_hard = 2
success = int(input('what you pay'))

if success >= hard:
    print(f'god would bless you, and you will success')
elif no_hard < success < hard:
    print(f'if you want to normal life,that is ok')
else:
    print(f"nothing you can do, even you not deserved to living this world")
