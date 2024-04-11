# 小枫
# @Time : 2024/3/16 15:00
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

# 1.create the tuple
nums = (10, 20, 90, 120, 779)
tub = (100,)  # it is important to add a ',' to avoid the error, maybe because the tuple's use () to involve.
error = (100)
print(tub)
print(error)
# 2. check the tuple
print(nums[4])
print(nums[2:4])
print(len(nums))
print(nums.index(20))

if 70 in nums:
    print('exist')
else:
    print('no')

i = 0
while i < len(nums):
    '''
    it is very cool!!!!
    I think this method using the index to present the object is amazing.
    And print must be the above of i += 1, if not we should change the condition
    '''
    print(nums[i])

    """ 
    do you understand how to calculate the number with its sign?
    sign of number present the sequence of the number and the length of group.
    """
    i += 1
