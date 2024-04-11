# 小枫
# @Time : 2024/3/18 13:29
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

import cv2

# read a picture
img = cv2.imread('xgxym.10.png')

# create a window, and named window,, WINDOW_MORMAL can make the window adjested
cv2.namedWindow("Face Recognition", cv2.WINDOW_NORMAL)
# modify the size of window
cv2.resizeWindow("Face Recognition", 300, 200)

# cv2.imshow("Face Recognition", 0)
cv2.imshow("Face Recognition", img)# 0 mean that there is no picture now
# remember to close your window
# waitKey mean waiting key(maybe you can use any button to close a window), 0 show not time to wait. other int show the time of window close
key = cv2.waitKey(0)  # I still can understand why I press any button the window close
# return ascii's value
# ord function can return ascii of sign
if key == ord("q"):  # if time is not 0, the ord will be used
    cv2.destroyAllWindows()
