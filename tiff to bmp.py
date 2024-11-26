import os
from PIL import Image

def convert_tiff_to_bmp(source_folder, target_folder):
    """
    批量将tiff文件格式转换为bmp格式，并将转换后的文件保存到新的文件夹中。

    :param source_folder: 原始tiff文件所在的文件夹路径
    :param target_folder: 转换后bmp文件保存的文件夹路径
    """
    # 检查目标文件夹是否存在，不存在则创建
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.tiff') or filename.lower().endswith('.tif'):
            source_path = os.path.join(source_folder, filename)
            target_path = os.path.join(target_folder, os.path.splitext(filename)[0] + '.bmp')

            try:
                # 打开tiff文件并转换为bmp格式
                with Image.open(source_path) as img:
                    img.save(target_path, format='BMP')
                print(f"成功转换：{filename} -> {os.path.basename(target_path)}")
            except Exception as e:
                print(f"转换失败：{filename}，错误信息：{e}")

if __name__ == "__main__":
    # 指定源文件夹和目标文件夹路径
    source_folder = r"C:\Users\za\Desktop\AVIZO project\tuiliqi scan 10pa parallel\change name\abstract"  # 替换为实际的源文件夹路径
    target_folder = r"C:\Users\za\Desktop\AVIZO project\tuiliqi scan 10pa parallel\change name\abstract\bmp"  # 替换为实际的目标文件夹路径

    # 调用转换函数
    convert_tiff_to_bmp(source_folder, target_folder)

