# 马士兵教育
# @Time : 2022/7/27 20:33
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project04

import cv2

# 输出一个视频文件：mp4，avi等
# 定义输出的视频格式VideoWriter_fourcc就是解包操作 等同于  'm', 'p', '4', 'v'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# 定义一个输出视频的文件
vw = cv2.VideoWriter('my_video000.mp4', fourcc, 25, (640, 480))

# 打开视频设备
cap = cv2.VideoCapture(0)

# 创建一个创建，并给窗口取名
# WINDOW_NORMAL可以让窗口大小变得可以调节
cv2.namedWindow('laoxiao', cv2.WINDOW_NORMAL)
# 修改窗口大小
cv2.resizeWindow('laoxiao', 800, 600)

# 循环来读取每一帧图片
while True:
    # 从摄像头读取视频,返回两个值， 第一个：是否读取到图片；第二个： 一帧图片
    flag, img = cap.read()

    # 将视频帧放在窗口中显示
    cv2.imshow('laoxiao', img)

    # 把一帧一帧的图片，写入到视频文件中
    vw.write(img)
    # 关闭窗口
    # waitKey方法表示等待按键, 0表示任何按键, 其他整数表示等待按键的时间,单位是毫秒, 超过时间没有发生按键操作窗口会自动关闭.
    key = cv2.waitKey(1)
    # 会返回按键的ascii的值:int
    # ord 函数就是返回一个符号的ascii值
    if key == ord('q'):
        break  # 用户输入q键，然后退出循环


# 释放
cap.release()
# 是否视频文件的写入IO
vw.release()
cv2.destroyAllWindows()




