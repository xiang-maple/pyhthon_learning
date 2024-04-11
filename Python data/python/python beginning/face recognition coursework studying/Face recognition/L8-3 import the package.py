# 小枫
# @Time : 2024/3/18 11:21
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

"""first way"""
# import First.mod1
# import First.xiaoxiao
#
# First.mod1.Hello_module()
#
# First.xiaoxiao.test1(1, 3)

"""second"""
from First import *  # if i use it, but i haven't use all, so i can't use the module.
# mod1.Hello_module()

xiaoxiao.test1(1, 2)
xiaoxiao.test2(2, 4)
#  how to only use a function in a module?
from First import mod1
mod1.Hello_module()

