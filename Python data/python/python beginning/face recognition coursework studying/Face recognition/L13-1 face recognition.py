# 小枫
# @Time : 2024/3/19 11:22
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

import cv2
# load the picture
img = cv2.imread('../../../../study way/huge.png')
# bilateral noise reduction
imgp = cv2.bilateralFilter(img, 3, 0.0001, 0.1)  # why I can't recognize some face






# 1. creat a harr cascade classifier
facer = cv2.CascadeClassifier('../../../../study way/haarcascade_frontalface_alt2.xml')
# 2. import the picture and graying
# img = cv2.imread('huge.png')
gray = cv2.cvtColor(imgp, cv2.COLOR_BGR2GRAY)

# 3. achieve face recognition
face = facer.detectMultiScale(gray)  # this step change the face in data

# print(face)
# output the place and (w and h)

for (x, y, w, h) in face:
    # useing the red rectangle to sign the face
    # [[203  42  60  60]]
    cv2.rectangle(imgp, (x, y), (x+w, y+h), (0, 0, 255), 2)
    # # use  the red ellipse
    # center = (x + w//2, y + h//2)
    # wh = (w//2, h//2)
    # cv2.ellipse(imgp, center, wh, 0, 0, 360, (0, 0, 255), 1)

cv2.imshow('face recognition', imgp)
cv2.waitKey(0)
cv2.destroyAllWindows()

