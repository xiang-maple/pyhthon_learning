# 小枫
# @Time : 2024/3/19 8:23
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

import cv2
# import a picture
img = cv2.imread('xgxym.10.png')
# img = cv2.imread('xgxym.10.png', 1)  # read the origin picture
# First way
# img = cv2.imread('xgxym.10.png', 0)  # adopt mean to graying

# Second way
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('xiang', gray_img)
print(gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

