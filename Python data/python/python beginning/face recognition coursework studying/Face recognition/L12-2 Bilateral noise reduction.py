# 小枫
# @Time : 2024/3/19 9:47
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

import cv2

# load the picture
img = cv2.imread('../../../../study way/huge.png')
# bilateral noise reduction
result = cv2.bilateralFilter(img, 3, 0.1, 1)
cv2.imshow('xiang', result)

cv2.waitKey(0)
cv2.destroyAllWindows()