# 马士兵教育
# @Time : 2022/7/20 15:16
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project03

# 第一种
import pkg1.mod2
import pkg1.mod3

pkg1.mod2.print_hello()
pkg1.mod3.print_hello()

# 第二种
# from pkg1 import *
# mod2.print_hello()
# mod3.print_hello()