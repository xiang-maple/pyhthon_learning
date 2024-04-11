from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from joblib import dump
import numpy as np
import cv2
import os

def load_data_and_labels(image_folder):
    images = []
    labels = []
    label_names = {}
    label_mapping = {}
    label_index = 0
    # 遍历文件夹中的每个人
    for person_name in os.listdir(image_folder):
        person_folder = os.path.join(image_folder, person_name)
        if not os.path.isdir(person_folder):
            continue  # 跳过非目录文件
        # 更新标签映射
        label_mapping[person_name] = label_index
        for image_name in os.listdir(person_folder):
            image_path = os.path.join(person_folder, image_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            if image is not None:
                images.append(image.flatten())
                labels.append(label_index)
        label_names[label_index] = person_name
        label_index += 1
    return np.array(images), np.array(labels), label_names

# 调整路径以指向新的图片存放位置
image_folder = 'face'
X, y, label_names = load_data_and_labels(image_folder)

# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 使用找到的最佳参数
pca = PCA(n_components=41, whiten=True, random_state=42)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# 训练KNN分类器
knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train_pca, y_train)

# 评估模型
y_pred = knn.predict(X_test_pca)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 保存PCA对象、KNN模型和标签名字映射
model_save_folder = 'models'  # 模型保存文件夹的相对路径
if not os.path.exists(model_save_folder):
    os.makedirs(model_save_folder)

dump(pca, os.path.join(model_save_folder, 'pca.joblib'))
dump(knn, os.path.join(model_save_folder, 'knn.joblib'))
dump(label_names, os.path.join(model_save_folder, 'label_names.joblib'))
