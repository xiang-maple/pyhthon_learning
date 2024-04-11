# 小枫
# @Time : 2024/3/16 11:56
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

print('the operation of list')
# 1.create the list
lst = ['abc', 12, 1.24, [10, 20]]
nums = [10, 20, 30, 40, 100, 90]
my_emt = []
only = [10,]
kiss = [10]
list1 = [1, 2, 3, 4, 5, 'awm, 1.23', 1.23, {13, 88}, [666], (23, 23), 66]
print(only)
print(kiss)  # this is different from the tuple
# 2.check the list
print(nums[0])  # use the index to check the element.
print(nums[2:5])  # pay attention to that 5 is not included, which is similar to range.
print(nums[-4:-1])  # the reverse index way!!!
print(nums[1])
print(nums[1:4])
print(nums[-5:-2])
print(nums.index(40))  # we use num.index to check the index of the elements.
print(nums.index(100))
print(len(nums))
print(len(list1))

# we use in to judge whether the element is in the list
if 70 in nums:
    print("70 is in list")
else:
    print('70 is not in list')

# Loop traversal
s = 0
for i in nums:
    # s = 0 a try for the  accumulation of i, but it is wrong and I should learn a lot to solve it
    s += i
    print(i)
print(s)


t = 0
while True:
    t += 1
    print(nums[t-1])
    if t >= len(nums):
        break

# s = my_emt
# I still can not understand how to use while to traversal
# while len(s) < len(nums):
#     s += nums
#     print(s)
# q = 0
# while q < len(nums):
#     q = nums
#     print(q)
# what the answer of while loop

#  3.add the list
nums.append(190)  # this step automatically add the number to the last of list
nums.append(999)

nums.insert(0, 80)  # add the object in any place.
nums.insert(8, 998)
print(nums)
nums.insert(9, 998)
nums.append('good for all day')
print(nums)
# 4.delete the list
nums.pop(2)  # delete the specific object, but debug delete the last object.
nums.pop(8)
nums.remove(10)  # delete the value of list
nums.remove(100)
print(nums)
# 5. modelify the list
nums[1] = 44
nums[0] = "kaixing"

print(nums)  # we use the = to modify the value
