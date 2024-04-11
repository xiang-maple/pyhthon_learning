# 小枫
# @Time : 2024/3/22 11:50
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : Python data
import cv2 as cv
unk = cv.imread('huge.png')
fd = cv.CascadeClassifier('haarcascade_frontalface_alt2.xml')
gyfd = cv.cvtColor(unk, cv.COLOR_BGR2GRAY)
imalld = fd.detectMultiScale(gyfd)

for (x, y, w, h) in imalld:
    temple = unk[y+h, x+w]
cv.imread('xiang', temple)
key = cv.waitKey(0) &0xFF
if key == ord('q'):
    cv.destroyAllWindows()