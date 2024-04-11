# 小枫
# @Time : 2024/3/18 13:56
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

import cv2
#  0 mean the default capture of computer if you add 1 it mean that you use a new capture
cap = cv2.VideoCapture(0)

# read a picture
# img = cv2.imread('xgxym.10.png')

# create a window, and named window
cv2.namedWindow("Face Recognition", cv2.WINDOW_NORMAL)
# modify the size of window
cv2.resizeWindow("Face Recognition", 300, 200)

# loop to read every picture of times
while True:
    # reture two values. First is whether read the pciture, second is a picture
    flag, img = cap.read()
    # show picture of video in window
    cv2.imshow("Face Recognition", img)# 0 mean that there is no picture now
    # remember to close your window
    # waitKey mean waiting key, 0 show any buttons. other int show the time of waiting button,the unit is ms.
    key = cv2.waitKey(1)  # this we can press any button to over a loop
    # return ascii's value
    # ord function can return ascii of sign
    if key == ord("q"):
        break  # user input q to end up the loop

cap.release()
cv2.destroyAllWindows()