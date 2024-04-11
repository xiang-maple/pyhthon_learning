# 小枫
# @Time : 2024/3/19 8:23
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

import cv2
# import a picture
img = cv2.imread('xgxym.10.png')
# img = cv2.imread('xgxym.10.png', 1)
# First way
grey_img = cv2.imread('xgxym.10.png', 0)  # adopt mean to graying

# Second way
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# binaryzation of picture. Returning two value: first is threshold, second is the image of binaryzation.
# tre_value, binary_img = cv2.threshold(grey_img, 80, 255, cv2.THRESH_BINARY)
# print(tre_value)

# adopt OTSU algorithm: -for automatic gain the great threshold
tre_value, binary_img = cv2.threshold(grey_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(tre_value)
cv2.imshow('xiang', binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

