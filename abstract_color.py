import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from PIL import Image

# 输入和输出文件夹路径
input_folder = r'C:\Users\za\Desktop\He\He'  # 原始图像所在的文件夹
output_folder = r'C:\Users\za\Desktop\He\He\He'  # 处理后图像保存的文件夹

# 创建输出文件夹（如果不存在的话）
os.makedirs(output_folder, exist_ok=True)

# 设置温度范围
min_temp = 20  # 最小温度（20℃）
max_temp = 25  # 最大温度（25℃）

# 获取输入文件夹中所有的 .tiff 文件
input_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.tiff')]

# 循环处理每一个图像文件
for input_file in input_files:
    # 拼接完整的输入和输出文件路径
    input_image_path = os.path.join(input_folder, input_file)
    output_image_path = os.path.join(output_folder, f"mapped_{input_file}")

    # 读取灰度图像
    img = Image.open(input_image_path)
    gray_image = np.array(img)

    # 设置灰度值映射，使用指定的温度范围
    norm = Normalize(vmin=min_temp, vmax=max_temp)
    cmap = cm.viridis  # 你可以选择其他的颜色映射，如 'plasma', 'inferno' 等

    # 创建映射后的图像
    fig, ax = plt.subplots(figsize=(6, 6))
    cax = ax.imshow(gray_image, cmap=cmap, norm=norm)
    colorbar = fig.colorbar(cax)  # 添加colorbar

    # 设置colorbar刻度，并标注为20℃和25℃
    colorbar.set_ticks([min_temp, max_temp])  # 设置刻度为最小值和最大值
    colorbar.set_ticklabels([f'{min_temp}℃', f'{max_temp}℃'])  # 设置刻度标签为20℃和25℃

    # 去除坐标轴
    ax.axis('off')

    # 保存映射后的图像到新的文件夹
    plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0)
    plt.close(fig)  # 关闭图形窗口

    print(f"处理完成: {input_image_path} -> {output_image_path}")

print("所有图像处理完成！")
