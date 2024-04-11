# 小枫
# @Time : 2024/3/15 20:16
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python studying pro

"""
compute the sum of all even number from 1 to 100
"""

# firstly, adopt while loop

i = 1
result = 0
# while i <= 100:
#     i += 1

# if i % 2 == 0:
# result += i

# print(result)

# # second: adopt while loop + break
# while True:  # True loop
#     i += 1
#     if i > 100:
#         break  # stop the loop
#     if i % 2 == 0:
#         result += i
# print(result)  # if the print is in the loop, it will shou all the data at every loop


# print(result)
#
# third: adopt while loop + continue

while i <= 100:
    i += 1  # variable i accumulate 1 for changing
    if i % 2 == 1:  # is odd number
        continue
    result += i  # accumulate
#
# print(result)
#
# # fourth: adopt for loop
# for i in range(1,101):  # range don't include the last number but first.
#     if i % 2 == 0:
#         result += i

print(result)
#
