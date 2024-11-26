import os
import shutil

# 原始文件夹路径
source_folder = r"C:\Users\za\Desktop\AVIZO project\tuiliqi scan 10pa parallel\change name\abstract"  # 替换为存放原始文件的文件夹路径
# 新文件夹路径
destination_folder = r"C:\Users\za\Desktop\AVIZO project\tuiliqi scan 10pa parallel\change name\abstract\bmp"  # 替换为存放改名文件的文件夹路径

# 确保目标文件夹存在
os.makedirs(destination_folder, exist_ok=True)

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    if filename.endswith(".tiff"):
        try:
            # 提取文件名前的数字部分
            original_number = float(filename[:-5])  # 去掉".tiff"部分
            # 新的文件名数字部分
            new_number = round(original_number + 9, 1)  # 加9，并保留1位小数
            # 生成新的文件名
            new_filename = f"{new_number}.tiff"
            # 复制并改名到目标文件夹
            shutil.copy(
                os.path.join(source_folder, filename),
                os.path.join(destination_folder, new_filename),
            )
            print(f"已将文件 {filename} 重命名并复制为 {new_filename}")
        except ValueError:
            print(f"文件 {filename} 的命名格式有问题，无法处理")