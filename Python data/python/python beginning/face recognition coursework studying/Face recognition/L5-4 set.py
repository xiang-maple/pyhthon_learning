# 小枫
# @Time : 2024/3/16 15:41
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

# 1. create a set
set1 = {1, 2, 3, 4}
set2 = {}
# 2. check
if 60 in set1:
    print("exist")
else:
    print('no')

# i = 0
# while i <= len(set1):
#     i += 1
# print(set1[i])  # so no callable, so we only use for circulate
for i in set1:
    print(i)
# t = 0
# while t <= len(set1):
#     t += 1
# print(set1(t))
# 3. add
set1.add(50)
set1.add(80)
set1.add(90807)
set1.add("kuku")
print(set1)

set1.update([666, 555])  # add many objects
print(set1)
# 4. delete
set1.remove(1)
print(set1)
# del (set1) how to use delete to compute
# 5. modify
set1.remove(555)
set1.add(100)
print(set1)
