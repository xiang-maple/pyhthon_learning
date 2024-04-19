# xiang-maple

"""operator"""
"""
---the data type with arithmatic operator 
"""
a = 0.1 * 0.1
print(a, type(a))  # float have 17 point precision
b = 4 / 2  # When division, the result default is float
print(b, type(b))

"""
--- the usage of arithmatic operator
"""
c = -7//2
print("c",c)

d = -7%2
print(d)

# divmod() attain two value
e, f = divmod(7, 2)
print(e)  # // outcome
print(f)  # % outcome
# superiority
# one unit is high two unit except **

"""
---position operator 
"""

# &
# |
# ^

# << and >>
ts = 63
print("ts:", ts, " ts << 2 is:", ts << 2)
print(bin(ts))
print("ts:", ts, " ts << 2 is:", ts >> 2)  # normal is divid 2**m but if you move out of the range, it will wrong
print(bin(ts >> 2))

"""
---superiority in the logical operator
"""

# and
# or
# not

# bool principle
print(1 and 3)
print(3 and 1)
print(0 and 3)
print(1 and 0)
print(0 or 3)
print(1 or 0)
print(1 or 3)
print(3 or 1)
print(not 3)

# the superiority
# not > and > or
print(1 or 3 and not 3 and 4 or 3)

"""
---member operator
"""
str = "xiang-maple"
print("xiang" in str)
print("Xiang" in str)
print("maple" not in str)

"""
--- identity operator
"""
lov = "xiang-maple"
print(id(lov))

# is check their id whether same or not
# is not
lv = 521
lvf = 521
print(lv is lvf)
print(lv is not lvf)
print(f"{id(lv)}\n{id(lvf)}")
# but in python is not same the range is [-5, 256]
# int pycharm is [-notend, +notend]

