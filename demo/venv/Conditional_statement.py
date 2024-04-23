# @Author: Xiang-Maple
# @Time: 2024/4/23 21:19
# @File: Conditional loop
# @Software: PyCharm

"""---If condition---"""
"""
-single branch if statment
"""
# light = "yellow"
# if light == "green":
#     print("please go")
# if light == "yellow":
#     print("stop")
# if light == "red":
#     print("stop")

"""
-more branchs if statment
"""
# two branches
# light = "green"
# if light == "green":
#     print("please go")
# else:
#     print("stop")

# more (three or more) branches
# light = "red"
# if light == "red":
#     print("stop")
# elif light == "green":
#     print("please go")
# else:
#     print("stop")

"""
-nested if
"""
# light = "green"
# pedestrian = 1
# if light == "green":
#     if pedestrian == 1:
#         print("you can go or turn")
#     else:
#         print("you can go but no turn")
# else:
#     print("stop")

"""---real usage in programming---"""
"""
- all way
"""
# score = 90
# if score <= 100 and score > 90:
#     print("your scale is A")
# if score >= 80 and score <= 90:
#     print("your scale is B")
# if score >= 60 and score < 80:
#     print("you scale is C, you can pass the test")
# if score < 60:
#     print("you have not pass the test")
"""
- python special way 
"""
# score = 99
# if 90 < score <= 100:
#     print("you scale is A")
# elif 80 <= score <= 90:
#     print("your scale is B")
# elif 60<= score < 80:
#     print("you scale is C, you pass the exam")
# else:
#     print("you have not pass the exam")
