# 马士兵教育
# @Time : 2022/6/29 14:12
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project02

print('======== 列表的各种操作 ==========')

# 1、 创建列表
lst = ['abc', 12, [10, 20]]
nums = [10, 20, 30, 40, 50, 60]
my_emt = []
# 2、查询列表
print(nums[3])  # 使用下标来查找单个元素
# 切片：使用下标来查找多个元素
print(nums[1:5])
print(nums[-5: -1])

print(nums.index(50))  # 返回单个元素的下标

# 返回列表的长度
print(len(nums))

# 判断是否存在
if 20 in nums:
    print("20在列表中")
else:
    print("不在列表中")

# 循环遍历
for i in nums:
    print(i)

# 3、新增操作
nums.append(70)  # 在列表最后面追加新元素
nums.insert(0, 80)  # 在任意位置插入新元素
print(nums)
# 4、删除操作
nums.pop(0)  # 删除指定下标的数据，默认删除最后一个元素

nums.remove(10)  # 删除列表中指定数据
print(nums)
# 5、修改操作
nums[2] = 400
print(nums)
