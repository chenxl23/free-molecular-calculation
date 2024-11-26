import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 批量处理函数
def batch_image_subtraction(background_path, input_folder, output_folder):
    # 读取本底图片
    background_image = Image.open(background_path)
    background_array = np.mean(np.array(background_image), axis=2)  # 转为灰度图

    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有 TIFF 图片
    for filename in os.listdir(input_folder):
        if filename.endswith(".tiff") or filename.endswith(".tif"):
            input_path = os.path.join(input_folder, filename)
            # 读取输入图片
            input_image = Image.open(input_path)
            input_array = np.mean(np.array(input_image), axis=2)  # 转为灰度图

            # 执行减法
            difference = np.clip(input_array - background_array, 0, 255).astype(np.uint8)

            # 转换为图片并保存
            output_image = Image.fromarray(difference)
            output_path = os.path.join(output_folder, f"{filename}")
            output_image.save(output_path)

    print(f"所有图片已处理完成，结果保存在：{output_folder}")

# 示例用法
background_path = r'C:\Users\za\Desktop\He\本底.tiff'  # 本底图片路径
input_folder = r'C:\Users\za\Desktop\He'  # 输入图片文件夹路径
output_folder = r'C:\Users\za\Desktop\He\He'  # 输出图片文件夹路径

batch_image_subtraction(background_path, input_folder, output_folder)
