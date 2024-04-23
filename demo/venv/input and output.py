# @Author: Xiang-Maple
# @Time: 2024/4/15 19:50
# @File: input and output
# @Software: PyCharm

"""---format outpur---"""
"""
-- First way %
"""
age = 19
# print("my age is %d" %age)
name = "coxi"
# print("my name is %s" %name)
#
# print("my name is %s,my age is %d"%(name,age))

"""
-- Second format()
"""
# 1. sequence get
str = "my name is {}, me age is {}".format(name,age,age)  # the age is waiting the next {}?
### str = "my name is{}, me age is {}",name age,age  # error
print(str)

# 2. index get
str1 = "my name is {0}, me age is {2}".format(name,age,age)
print(str1)

# 3. keyword get
str3 ="my name is {name}, me age is {age}".format(age=19,name="Coxi")

# 4. dicmap get
info = {"name": "coxi", "age": 19}
str4 ="my name is {name}, me age is {age}".format(**info)
print(str4)

# 5. listmmap get
lst = [19,"Coxi"]
str5 = "my name is {1}, me age is {0}".format(*lst)
print(str5)
str6 = "my name is {0[1]}, me age is {0[0]}, this year is {1}".format(lst,2024)
print(str6)

# 6. number change
print("yuanzhoulv{:.2f}".format(3.1415926535))
print("{:.2e}".format(39000100))  # this way will delete the value,100 is deleted
print("{:.1%}".format(0.4))
print("{:*>10}".format("coxi"))
print("{:*<10}".format("coxi"))
print("{:*^10}".format("coxi"))

