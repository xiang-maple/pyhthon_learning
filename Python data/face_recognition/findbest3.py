from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import cv2
import os

def load_data_and_labels(image_folder):
    images = []
    labels = []
    label_names = {}
    label_mapping = {}
    label_index = 0
    for person_name in os.listdir(image_folder):
        person_folder = os.path.join(image_folder, person_name)
        if not os.path.isdir(person_folder):
            continue  # Skip if it's not a directory
        for image_name in os.listdir(person_folder):
            image_path = os.path.join(person_folder, image_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            if image is not None:
                images.append(image.flatten())
                labels.append(label_index)
        label_names[label_index] = person_name
        label_mapping[person_name] = label_index
        label_index += 1
    return np.array(images), np.array(labels), label_names

# 设置图片存放位置的相对路径
image_folder = 'images/after'
X, y, label_names = load_data_and_labels(image_folder)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 初始化一个字典来存储准确率，键为(n_components, n_neighbors)元组
accuracy_scores = {}

# 遍历不同的n_components值
for n_components in range(1, min(len(X_train), len(X_test)) + 1):
    pca = PCA(n_components=n_components, whiten=True, random_state=42)
    X_train_pca = pca.fit_transform(X_train)
    X_test_pca = pca.transform(X_test)
    
    # 内层循环：遍历不同的n_neighbors值
    for n_neighbors in range(1, 21):
        knn = KNeighborsClassifier(n_neighbors=n_neighbors)
        knn.fit(X_train_pca, y_train)
        
        y_pred = knn.predict(X_test_pca)
        accuracy = accuracy_score(y_test, y_pred)
        
        # 记录当前n_components和n_neighbors的准确率
        accuracy_scores[(n_components, n_neighbors)] = accuracy

# 找到准确率最高的参数组合
best_params = max(accuracy_scores, key=accuracy_scores.get)
best_n_components, best_n_neighbors = best_params
best_accuracy = accuracy_scores[best_params]

print(f"Best parameters: n_components = {best_n_components}, n_neighbors = {best_n_neighbors}, Accuracy = {best_accuracy}")
