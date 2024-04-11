import cv2
import os
import numpy as np

# 定义输入和输出文件夹的相对路径
input_folder = 'face'
output_folder = 'images/after'
target_size = (100, 100)

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 加载OpenCV的预训练人脸检测模型
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 遍历每个人的子文件夹
for person_name in os.listdir(input_folder):
    person_folder = os.path.join(input_folder, person_name)
    # 创建相应的输出子文件夹
    output_person_folder = os.path.join(output_folder, person_name)
    if not os.path.exists(output_person_folder):
        os.makedirs(output_person_folder)

    # 遍历子文件夹中的所有图片
    for img_name in os.listdir(person_folder):
        img_path = os.path.join(person_folder, img_name)
        img = cv2.imread(img_path)
        if img is None:
            continue
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 检测图片中的人脸
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if faces is not None and len(faces) > 0:
            x, y, w, h = faces[0]
            face = img[y:y+h, x:x+w]
            resized_face = cv2.resize(face, target_size)

            # 图像增强：亮度与对比度调整
            alpha = 1.2  # 对比度控制
            beta = 20    # 亮度控制
            enhanced_face = cv2.convertScaleAbs(resized_face, alpha=alpha, beta=beta)

            # 图像增强：高斯模糊
            blurred_face = cv2.GaussianBlur(enhanced_face, (5, 5), 0)

            # 保存处理后的图像到相应的输出子文件夹
            output_path = os.path.join(output_person_folder, img_name)
            cv2.imwrite(output_path, blurred_face)

print("人脸检测、裁剪和图像增强完成。")
