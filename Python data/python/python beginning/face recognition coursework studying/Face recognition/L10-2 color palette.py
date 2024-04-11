# 小枫
# @Time : 2024/3/18 21:23
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

import cv2
import numpy as np

cv2.namedWindow('xiang', cv2.WINDOW_NORMAL)
cv2.resizeWindow('xiang', 800, 600)


# returning function
def call_back(value):
    print(value)


# create three track bar, RGB
cv2.createTrackbar("R", 'xiang', 0, 255, call_back)
cv2.createTrackbar("G", 'xiang', 0, 255, call_back)
cv2.createTrackbar("B", 'xiang', 0, 255, call_back)

# create the background of color palette: black
img = np.zeros((800, 600, 3), dtype=np.uint8)  # so the pixel format is different from the normal

while True:

    # gain the value of RGB trackbar.
    r = cv2.getTrackbarPos('R','xiang')
    g = cv2.getTrackbarPos('G','xiang')
    b = cv2.getTrackbarPos('B','xiang')

    # slice, if I not write, it mean that we start and end in default.
    img[:] = [b, g, r]  # because of opencv sequence of bgr

    cv2.imshow('xiang', img)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
