import os
import re

# 指定需要遍历的文件夹路径
folder_path = r'D:\Python data\face_recognition\face'  # 请替换为你的实际文件夹路径

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 使用正则表达式匹配"任意文本(数字)"的文件名格式
    match = re.match(r'(.+)\((\d+)\)(\.\w+)?$', filename)
    if match:
        # 构造新的文件名格式"任意文本_数字.扩展名"
        new_filename = f"{match.group(1)}_{match.group(2)}{match.group(3) if match.group(3) else ''}"
        # 构造完整的旧文件路径和新文件路径
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{filename}' to '{new_filename}'")
