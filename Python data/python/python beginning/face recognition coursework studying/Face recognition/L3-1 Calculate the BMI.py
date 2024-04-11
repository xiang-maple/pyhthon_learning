# 小枫
# @Time : 2024/3/15 14:38
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python studying pro

# all the input function are str type
h = input('please output the height:the unit is meter')  # they both str, we tend to transform them

w = input('please output the weight:the unit is kilograms')

name = input('please write your name')
age = int(input('please input your age'))
h = float(h)
w = int(w)
print(h)
print(w)
print(type(h))
print(type(w))  # if we have print(a), then we want to add a type, so we should input type directly.
# if you want to quick annotation you can use ctrl+/.
"""compute the BMI"""
bmi = w/h**2  # if I annotation the int and float, it will indicate unsupported operand type(s) for ** or pow(): 'str' and 'int'. mean that the ** process is wrong
print(bmi)
# we only keep it to the last decimal place.

"""computation of python"""

"""1. arithmetic operator"""
print(2**8)
ss = 2/3
print(2/3)
print('%.3f' % ss)
print(10//3)
print(1+2-3)
print(1*3)
print(9 % 2)  # you should pay attention to the white space for %
# please pay attention the superiority of the arithmetic operators.
print((8+9)*3**2/2-8)
print((8+9)*3**(2/2)-8)
"""2. assignment operator"""
a = 100
b, c, d, p = 10, 30, 50, 'hellp world'
e, f = 1000, 10000
g = h = 1000

"""3. compound assignment operator"""

"""
1. 10 
2. a original is 100
3 a + 10 =  new a =110
"""

a += 10
a += 10 + 5
b -= 3
c *= 5
d **= 2
e %= 99
f //= 99
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


""" 
%.1f keep it to the last decimal place, %.2f keep it in two places after the decimal point.  
I don't understand what is the % bmi.
"""
# the output of python
# It is extremely important in python!
print('your bmi is: %.4f' % bmi)  # print('my name is: %s, my age is: %d' % (name, age))
print('your name is: %s, your age is: %d' % (name, age))
print("let me seesee: %010d" % f)
# also the output by {} is ok
print(f'weight:{w} and height:{h}')  # but it must be str
print('*', end="")  # I don't understand! 结束符不懂 思密达
print(f'name:{name} and age:{age}')
