# @Author: Xiang-Maple
# @Time: 2024/4/15 18:55
# @File: input and output
# @Software: PyCharm
"""binary octal decimal hexdecmial"""
d10 =100
print(type(d10))
print(bin(d10))
print(oct(d10))
print(hex(d10))
b10 = 0b1100100
print(type(b10))  # still the integer
print(int(b10))
o10 = 0o144
print(int(o10))
h10 = 0x64
print(int(h10))

"""--bull--"""

# a = 3.14
# print(f"a={a}",type(a))
# # b = input("test bull type,please input b value: ")  # so the char is 1 in bull
# b = input("test bull type,please input b value: ")
# b = int(b)  # change the b into integer;
# if b:
#     print("haha")
#



"""--complex--"""
#
# c =complex(1,3)
# print(c,type(c))
# com = 1+3j
# print(com,type(com))



"""the type compulsory change(use to other)"""
# # int(): integer float bool nubmerstring !!!!no complex!!!!
# # float(): s^  # It mean same as above
# # complex(): s^
# # bool(): change all
#
# num1 = 1
# num2 = 3.14
# num3 = 3+4j
# num4 = "str"
# num5 = "c"
# num6 = True
# print(num5,type(num5))  # there are not char in python
"""--test--"""
# # vvvv
# int(num3)  # error
# float(num3)  # error
# complex()



"""bool is false condition"""
# b1 = bool({})
# print(b1)
# b2 = bool([])
# print(b2)
# b3 = bool(())
# print(b3)
# b4 = bool(0)
# print(b4)
# b5 = bool("")
# print(b5)
# b6 = bool(0.00)
# print(b6)
# b7 = bool(0+1j)
# print(b7)  # the answer is true
# b8 = bool(0+0j)
# b9 = bool(0j)
# print(b8)
# print(b9)

