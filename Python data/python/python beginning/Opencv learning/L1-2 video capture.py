# 小枫
# @Time : 2024/3/20 17:40
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python
'''capture gain'''
import cv2
import numpy as np
cv2.namedWindow('xiang', cv2.WINDOW_NORMAL)  # in default it is autosize
cv2.resizeWindow('xiang', 600, 480)
cap = cv2.VideoCapture(0)
fourcc = cv2.fourcc(*'XVID')

if not cap.isOpened():
    print("Can't open camera")
    exit()
while True:
    ret, frame = cap.read()  # ret is boolean value mean it is True of False
    if not ret:
        print("can't receive frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('xiang', gray)
    key = cv2.waitKey(1)  # the 1 mean 25ms
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()

        """你还可以使用cap.get(propId)方法访问该视频的某些功能，其中propId是0到18之间的一个数字。每个数字表示视频的属性（如果适用于该视频），并且可以显示完整的详细信息在这里看到：cv::VideoCapture::get()。其中一些值可以使用cap.set(propId，value)进行修改。value是你想要的新值。

例如，我可以通过cap.get(cv.CAP_PROP_FRAME_WIDTH)和cap.get(cv.CAP_PROP_FRAME_HEIGHT)检查框架的宽度和高度。默认情况下，它的分辨率为640x480。但我想将其修改为320x240。只需使用和即可。ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,320) and ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,240)."""


