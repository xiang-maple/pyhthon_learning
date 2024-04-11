# 小枫
# @Time : 2024/3/18 13:56
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

# import cv2
#
# # input a file of video, mp4, avi, and so on
# # just like to salvage the mp4v - 'm' 'p' '4' 'v'
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# # define a file to input video
# vw = cv2.VideoWriter('myvideo1.mp4', fourcc, 30, (600, 480))
#
# # open the capture
# cap = cv2.VideoCapture(0)
#
# # read a picture
# # img = cv2.imread('xgxym.10.png')
#
# # create a window, and named window
# cv2.namedWindow("Face Recognition", cv2.WINDOW_NORMAL)
# # modify the size of window
# cv2.resizeWindow("Face Recognition", 600, 480)
#
# # loop to read every picture of times
# while True:
#     # reture two values. First is whether read the pciture, second is a picture
#     flag, img = cap.read()
#     # show picture of video in window
#     cv2.imshow("Face Recognition", img)  # 0 mean that there is no picture now
#     # put every picture into the file of video
#     vw.write(img)
#     # remember to close your window
#     # waitKey mean waiting key, 0 show any buttons. other int show the time of waiting button,the unit is ms.
#     key = cv2.waitKey(1)
#     # return ascii's value
#     # ord function can return ascii of sign
#     if key == ord("q"):
#         break  # user input q to end up the loop
#
# cap.release()
# # release the IO of file
# vw.release()
# cv2.destroyAllWindows()
import cv2

facer = cv2.CascadeClassifier('../../../../study way/haarcascade_frontalface_alt2.xml')

img = cv2.imread('kun.2.jpeg')
result = cv2.bilateralFilter(img, 3, 0.000001, 0.0001)
new_img = result[35:102, 205:263]
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # this is for detect the face postion and size
# faces = facer.detectMultiScale(gray)
#
# for (x, y, w, h) in faces:
#     print(f'site of face:{x}, {y}')
#     print(f'the width of the face:{w}, the height of the face:{h}')
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
#
# cv2.imshow("test", img)
# cv2.waitKey(0)
cap = cv2.VideoCapture(0)
# read every picture
flag, my_img = cap.read()

while flag:
    gray = cv2.cvtColor(my_img, cv2.COLOR_BGR2GRAY)
    # test my face
    my_face = facer.detectMultiScale(gray)

    for (x, y, w, h) in my_face:
        x = x + 15
        w = w - 30
        # how to write the ai face change
        new_img = cv2.resize(new_img, dsize=(w, h))  # make the face and new face identified in weight and width
        # in order to replace more great, we use ellipse
        for i in range(h):  # in the matrix the first dimension is y
            for j in range(w):
                if (i - h//2)**2 + (j - w//2)**2 <= (w//2)**2:  # judge whether a point in the picture whether in the center of face circle.
                    my_img[y+i, x+j] = new_img[i, j]

    cv2.imshow('xiang', my_img)
    # read the next picture
    flag, my_img = cap.read()

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
