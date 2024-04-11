import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk
import subprocess
import os
import shutil

# 全局变量用于存储图像和预测标签的Label控件
image_panel = None
prediction_label = None

# 获得脚本所在的目录
script_dir = os.path.dirname(__file__)

def clear_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def preprocess():
    images_after_path = os.path.join(script_dir, 'images', 'after')
    clear_directory(images_after_path)
    work1_path = os.path.join(script_dir, 'work1.py')
    transtojpg_path = os.path.join(script_dir, 'transtojpg.py')
    subprocess.run(["python", work1_path], check=True)
    subprocess.run(["python", transtojpg_path], check=True)
    print("预处理完毕")

def train():
    training1_path = os.path.join(script_dir, 'training1.py')
    subprocess.run(["python", training1_path], check=True)
    print("训练完毕")

def show_image(image_path):
    global image_panel
    img = Image.open(image_path)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)
    if image_panel is None:
        image_panel = Label(app, image=img_tk)
        image_panel.image = img_tk
        image_panel.pack()
    else:
        image_panel.configure(image=img_tk)
        image_panel.image = img_tk

def show_prediction(prediction):
    global prediction_label
    if prediction_label is None:
        prediction_label = Label(app, text=prediction)
        prediction_label.pack()
    else:
        prediction_label.configure(text=prediction)

def inference():
    file_path = filedialog.askopenfilename()
    if file_path:
        destination = os.path.join(script_dir, 'infer.jpg')
        if os.path.exists(destination):
            os.remove(destination)  # 删除旧文件
        shutil.copy(file_path, destination)
        infer_path = os.path.join(script_dir, 'infer.py')
        result = subprocess.run(["python", infer_path], capture_output=True, text=True)
        prediction = result.stdout.strip()  # Assuming the script prints the prediction
        
        show_image(destination)
        show_prediction("预测的人脸是: " + prediction)

app = tk.Tk()
app.title("Face Recognition")
app.geometry("300x350")

preprocess_btn = tk.Button(app, text="预处理", command=preprocess)
preprocess_btn.pack(pady=5)

train_btn = tk.Button(app, text="训练", command=train)
train_btn.pack(pady=5)

inference_btn = tk.Button(app, text="推理", command=inference)
inference_btn.pack(pady=5)

app.mainloop()
