# 马士兵教育
# @Time : 2022/6/29 14:12
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project02

print('======== 字典的各种操作 ==========')

# 1、 创建字典
dict1 = {'a': 10, 'b': 20, 'c': 50}
dict2 = {}  # 创建一个空字典
# 2、查询操作
# 根据一个key返回对应的value---第一种
print(dict1['a'])
#  根据一个key返回对应的value——第二种
print(dict1.get('f'))
#  区别：如果key不存在，dict[key]会报错，get函数不会
dict1.keys()  # 遍历字典中所有的key
for k in dict1.keys():
    print(k)

for v in dict1.values():  # 遍历字典中所有的value
    print(v)

# 遍历字典中所有的元素（包括key和value）
for k, v in dict1.items():
    print(f"元素的key是:{k},对应的value:{v}")
# 3、新增操作
dict1['d'] = 100
print(dict1)
# 4、删除操作
del(dict1['b'])
# 5、修改操作
dict1['a'] = 500
print(dict1)
