# 小枫
# @Time : 2024/3/18 10:46
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

import First
""" the first case we don't set def in mod1, so we can use the def in init directly"""
First.Hello_module()

import First.xiaoxiao
"""if when we set the def in mod1, we can not use it as above from"""

First.xiaoxiao.test1(1, 3)  # this way is wrong because the xiao xaio is not in the init

