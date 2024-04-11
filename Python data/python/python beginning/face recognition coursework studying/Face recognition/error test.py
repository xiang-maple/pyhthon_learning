# 小枫
# @Time : 2024/3/21 11:34
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python
import cv2 as cv
img = cv.imread('kun.2.jpeg')
cv.namedWindow('xiang', cv.WINDOW_NORMAL)
cv.resizeWindow('xiang', 300, 250)
cv.imshow('xiang',img)
cv.waitKey(0)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()