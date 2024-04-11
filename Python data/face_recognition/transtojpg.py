import os

def rename_extensions_to_jpg(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 获取文件的完整路径
            old_file_path = os.path.join(root, file)
            # 分割文件名和扩展名，然后更改扩展名为.jpg
            new_file_path = os.path.join(root, os.path.splitext(file)[0] + '.jpg')
            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f'Renamed {old_file_path} to {new_file_path}')

# 设置目标目录的相对路径
directory = 'images/after'
rename_extensions_to_jpg(directory)
