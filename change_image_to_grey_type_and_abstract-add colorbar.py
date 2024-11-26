import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm  # 用于颜色映射
from matplotlib.colors import Normalize

# RGB 转灰度的加权平均法
def rgb_to_grayscale(image_array):
    return (0.2989 * image_array[:, :, 0] +
            0.5870 * image_array[:, :, 1] +
            0.1140 * image_array[:, :, 2])

# 批量处理函数
def batch_image_subtraction_with_colormap_and_colorbar(background_path, input_folder, output_folder):
    # 读取本底图片
    background_image = Image.open(background_path)
    background_array = rgb_to_grayscale(np.array(background_image))  # 转为灰度图

    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有 TIFF 图片
    for filename in os.listdir(input_folder):
        if filename.endswith(".tiff") or filename.endswith(".tif"):
            input_path = os.path.join(input_folder, filename)
            # 读取输入图片
            input_image = Image.open(input_path)
            input_array = rgb_to_grayscale(np.array(input_image))  # 转为灰度图

            # 执行减法
            difference = np.clip(input_array - background_array, 0, 255)  # 保证像素值范围在0-255
            difference_normalized = difference / 255.0  # 归一化到 [0, 1]

            # 创建绘图窗口并绘制图像
            fig, ax = plt.subplots(figsize=(8, 6))
            cax = ax.imshow(difference_normalized, cmap=cm.plasma, norm=Normalize(vmin=0, vmax=1))

            # 添加 colorbar 并设置刻度
            cbar = fig.colorbar(cax, ax=ax, orientation='vertical')
            cbar.set_ticks([0, 0.5, 1])  # 在归一化范围内添加刻度
            cbar.set_ticklabels(["20℃", "22.5℃", "25℃"])  # 自定义刻度标签

            # 去掉坐标轴
            ax.axis('off')

            # 保存图像
            output_path = os.path.join(output_folder, f"colored_with_colorbar_{filename}")
            plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
            plt.close(fig)  # 关闭图形窗口

            print(f"处理完成: {input_path} -> {output_path}")

    print(f"所有图片已处理完成，结果保存在：{output_folder}")

# 示例用法
background_path = r'E:\数据\20241124\Xe\本底.tiff'  # 本底图片路径
input_folder = r'E:\数据\20241124\Xe'  # 输入图片文件夹路径
output_folder = r'E:\数据\20241124\Xe\Processed'  # 输出图片文件夹路径

batch_image_subtraction_with_colormap_and_colorbar(background_path, input_folder, output_folder)


