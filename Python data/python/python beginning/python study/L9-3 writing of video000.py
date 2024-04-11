# 小枫
# @Time : 2024/3/18 13:56
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

import cv2

# input a file of video, mp4, avi, and so on
# just like to salvage the mp4v - 'm' 'p' '4' 'v'
forlie = cv2.VideoWriter_fourcc(*'mp4v')

# define a file to input video
vw = cv2.VideoWriter('myvideo5555.mp4', forlie, 30, (600, 480))

# open the capture
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
    cv2.imshow("Face Recognition", img)  # 0 mean that there is no picture now
    # put every picture into the file of video
    # vw.write(img)
    # remember to close your window
    # waitKey mean waiting key, 0 show any buttons. other int show the time of waiting button,the unit is ms.
    key = cv2.waitKey(1)
    # return ascii's value
    # ord function can return ascii of sign
    if key == ord("q"):
        break  # user input q to end up the loop

cap.release()
# release the IO of file
vw.release()
cv2.destroyAllWindows()
