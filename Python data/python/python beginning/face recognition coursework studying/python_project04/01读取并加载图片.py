# 马士兵教育
# @Time : 2022/7/27 20:33
# @Author : 肖斌老师
# @Version : 
# @IDE : PyCharm
# @Project : python_project04

import cv2

# 读取图片
img = cv2.imread('cat.jpeg')
# print(img)
# 创建一个创建，并给窗口取名
# WINDOW_NORMAL可以让窗口大小变得可以调节
cv2.namedWindow('laoxiao', cv2.WINDOW_NORMAL)
# 修改窗口大小
cv2.resizeWindow('laoxiao', 800, 600)
# 在窗口中加载和显示图片 ,0表示暂时没有图片
# cv2.imshow('laoxiao', 0)
cv2.imshow('laoxiao', img)

# 关闭窗口
# waitKey方法表示等待按键, 0表示任何按键, 其他整数表示等待按键的时间,单位是毫秒, 超过时间没有发生按键操作窗口会自动关闭.
key = cv2.waitKey(0)
# 会返回按键的ascii的值:int
# ord 函数就是返回一个符号的ascii值
if key == ord('q'):
    cv2.destroyAllWindows()




