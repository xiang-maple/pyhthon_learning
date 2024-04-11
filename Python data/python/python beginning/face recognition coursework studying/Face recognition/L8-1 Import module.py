# 小枫
# @Time : 2024/3/17 20:39
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python
"""
5 ways of importing modules
1. import modulename
2. from module_name import function_name
3. from module_name import *
4. import module_name as
5.from module_name import function_name as
"""

# import math  # first way
#
# print(math.log2(4))
#
# from math import log2  # second
#
# print(log2(4))

# from math import *  # third
#
# print(log2(26))
# print(log10(99))
#
# import math as xiao_xiang  # fourth
#
# print(xiao_xiang.log2(8))

from math import log10 as no  # fifth

print(no(10))
