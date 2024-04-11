# 小枫
# @Time : 2024/3/21 10:34
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python
import cv2 as cv
import numpy as np
import os
from PIL import Image
'''read and show the image'''
# img = cv.imread('kun.2.jpeg')
# cv.namedWindow('xiang', cv2.WINDOW_NORMAL)
# cv.resizeWindow('xiang', 300, 250)
# cv.imshow('xiang',img)
# cv.waitKey(0)
# if cv.waitKey(0) & 0xFF == ord('q'):
#     cv.destroyAllWindows()
'''find the face of image and sign it'''
img = cv.imread(r'D:\Python data\python\python beginning\face recognition coursework studying\Face recognition\huge.png')
img_gry = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imwrite('kun.3.jpeg', img_gry)  #  如果没有就直接创建，视频文件考虑解码

refacet = cv.CascadeClassifier("../../../../study way/haarcascade_frontalface_alt2.xml")
refaced = refacet.detectMultiScale(img_gry)
for (x, y, w, h) in refaced:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv.imshow('xiang', img)
cv.waitKey(0)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
'''name the face the write it in a new file as training'''



