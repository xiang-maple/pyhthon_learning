# 马士兵教育
# @Time : 2022/7/20 13:12
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project03

"""
导入模块的5中方式

1. import 模块名
2. from 模块名 import 函数名
3. from 模块名 import  *
4. import 模块名 as 别名
5. from 模块名 import 函数名 as 别名
"""
# 第一种
# import math
#
# print(math.log2(8))

# 第二种
# from math import log2
#
# print(log2(16))

# 第三种
# from math import *
#
# print(log2(26))
# print(log10(100))

# 第四种
# import math as mt
#
# print(mt.log2(8))

# 第五种
from math import log10 as ln

print(ln(100))