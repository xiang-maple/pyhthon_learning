# 小枫
# @Time : 2024/3/19 9:47
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

import cv2

# load the picture
img = cv2.imread('xgxym.10.png')
# there three
result = cv2.GaussianBlur(img, (3, 3), sigmaX=1)
cv2.imshow('xiang', result)

cv2.waitKey(0)
cv2.destroyAllWindows()