# 小枫
# @Time : 2024/3/19 15:08
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

import cv2

img = cv2.imread('kun.2.jpeg')

new_img = img[35:102, 205:263]

cv2.imshow('kun', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
