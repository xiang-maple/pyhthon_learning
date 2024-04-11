from joblib import load
import cv2
import numpy as np
import os  # 导入os模块

# 设定模型和标签名称的相对路径
base_path = os.path.dirname(__file__)  # 获取脚本文件所在的目录
pca_path = os.path.join(base_path, 'models', 'pca.joblib')
knn_path = os.path.join(base_path, 'models', 'knn.joblib')
label_names_path = os.path.join(base_path, 'models', 'label_names.joblib')

# 加载模型和标签名称
pca = load(pca_path)
knn = load(knn_path)
label_names = load(label_names_path)

# 定义预处理函数
def preprocess_image(image_path, target_size=(250, 250)):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img = cv2.imread(image_path)
    if img is None:
        print("不能加载图片")
        return None
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if faces is not None and len(faces) > 0:
        x, y, w, h = faces[0]
        face = img[y:y+h, x:x+w]
        resized_face = cv2.resize(face, target_size)
        return resized_face
    else:
        print("没有检测到人脸。")
        return None

# 定义预测函数
def predict_image(image_path):
    preprocessed_image = preprocess_image(image_path)
    if preprocessed_image is not None:
        gray_image = cv2.cvtColor(preprocessed_image, cv2.COLOR_BGR2GRAY)  # 确保转换为灰度图
        image_flatten = gray_image.flatten().reshape(1, -1)  # 转换成模型需要的形状
        image_pca = pca.transform(image_flatten)  # 应用PCA
        prediction = knn.predict(image_pca)  # 预测
        predicted_label = label_names[prediction[0]]
        print(f"预测的人脸是: {predicted_label}")
    else:
        print("预处理失败，无法预测。")

# 测试新图片，这里的路径也要改为相对路径
infer_path = os.path.join(base_path, 'infer.jpg')
predict_image(infer_path)
