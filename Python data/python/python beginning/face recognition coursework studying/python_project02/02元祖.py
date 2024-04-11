# 马士兵教育
# @Time : 2022/6/29 14:12
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project02

print('======== 元祖的各种操作 ==========')

# 1、 创建元祖
nums = (10, 20, 30, 40, 50, 60)
tub = (100,)  # 如果元祖中只有一个值，必须再后面加逗号

# nums[2] = 300
# 2、查询元祖
# 使用下标来查找单个元素
print(nums[4])
# 切片：使用下标来查找多个元素
print(nums[1:5])

# 返回单个元素的下标
print(nums.index(40))
# 返回元祖的长度
print(len(nums))

# 判断是否存在
if 20 in nums:
    print('存在')

# 循环遍历
i = 0
while i < len(nums):
    print(nums[i])
    i += 1
