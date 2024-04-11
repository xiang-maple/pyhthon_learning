# 小枫
# @Time : 2024/3/16 15:16
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

# 1.create dictionary
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {}  # create a hollow dictionary
# 2.check
# according to the key to find the value, first way
print(dict1["b"])
# second way
print(dict1.get('z'))  # so the second way is better than the first for it would report error.
dict1.keys()  # traversal all keys
for k in dict1.keys():
    print(k)
for v in dict1.values():
    print(v)
for s, t in dict1.items():
    print(s, t)
for abst in dict1.items():
    print(abst)
# 3.add
dict1['d'] = 100
dict1['hh'] = 1000
print(dict1)
# 4.delete
del (dict1['b'])
del (dict1['hh'])
# 5.modify
dict1['a'] = 100
dict1['d'] = 555
print(dict1)

