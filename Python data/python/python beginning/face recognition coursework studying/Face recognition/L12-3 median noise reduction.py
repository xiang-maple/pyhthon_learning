# 小枫
# @Time : 2024/3/19 9:47
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

import cv2

# load the picture
img = cv2.imread('noise.png')
# median noise reduction
result = cv2.medianBlur(img, 3)
cv2.imshow('xiang', result)

cv2.waitKey(0)
cv2.destroyAllWindows()