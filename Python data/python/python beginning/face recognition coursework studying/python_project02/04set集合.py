# 马士兵教育
# @Time : 2022/6/29 14:12
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project02

print('======== set的各种操作 ==========')

# 1、 创建set
set1 = {10, 20, 30, 60}
set2 = set()
# 2、查询操作
if 20 in set1:
    print('存在')
for i in set1:
    print(i)
# 3、新增操作
set1.add(50)  # 添加单个元素
set1.add(50)

set1.update([80, 90])  # 添加多个元素，参数必须是列表
print(set1)
# 4、删除操作
set1.remove(10)
print(set1)
# 5、修改操作(无法修改单个元素)

set1.remove(50)
set1.add(100)
print(set1)