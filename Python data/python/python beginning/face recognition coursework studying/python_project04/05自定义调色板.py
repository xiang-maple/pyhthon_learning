# 马士兵教育
# @Time : 2022/8/6 20:29
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project04

import cv2
import numpy as np

# 创建一个创建，并给窗口取名
# WINDOW_NORMAL可以让窗口大小变得可以调节
cv2.namedWindow('laoxiao', cv2.WINDOW_NORMAL)
# 修改窗口大小
cv2.resizeWindow('laoxiao', 800, 600)


# 自定义的回调函数
def call_back(value):
    print(value)


# 创建三个进度条，RGB
cv2.createTrackbar('R', 'laoxiao', 0, 255, call_back)
cv2.createTrackbar('G', 'laoxiao', 0, 255, call_back)
cv2.createTrackbar('B', 'laoxiao', 0, 255, call_back)

# 创建调色板的背景。一开始调色板背景的初始颜色为： 黑色.RGB都是0
# 图片的本质就是矩阵
img = np.zeros((600, 800, 3), dtype=np.uint8)

while True:

    # 获取三个进度条的值，其实就RGB的值
    r = cv2.getTrackbarPos('R', 'laoxiao')
    g = cv2.getTrackbarPos('G', 'laoxiao')
    b = cv2.getTrackbarPos('B', 'laoxiao')

    # 切片：， [开始位置:结束位置]
    img[:] = [b, g, r]

    cv2.imshow('laoxiao', img)
    # 关闭窗口
    # waitKey方法表示等待按键, 0表示任何按键, 其他整数表示等待按键的时间,单位是毫秒, 超过时间没有发生按键操作窗口会自动关闭.
    key = cv2.waitKey(1)
    # 会返回按键的ascii的值:int
    # ord 函数就是返回一个符号的ascii值
    if key == ord('q'):
        break

cv2.destroyAllWindows()
