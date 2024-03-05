import os

# 原始图片文件夹路径
original_folder_path = r'C:\Users\Administrator\Documents\AirSim\2024-01-18-17-34-57\mav0\cam0\test/'

# 目标图片文件夹路径
destination_folder_path = r'path_to_destination_images_folder/'

# 遍历原始图片文件夹中的文件
for filename in os.listdir(original_folder_path):
    # 构建原始图片文件的完整路径
    original_image_path = os.path.join(original_folder_path, filename)

    # 构建目标图片文件的完整路径
    destination_image_path = os.path.join(destination_folder_path, filename)

    # 重命名图片文件
    try:
        os.rename(original_image_path, original_image_path)
        # print(f'Renamed {original_image_path} to {destination_image_path}')
    except FileNotFoundError:
        a=1
        # print(f'Error: {original_image_path} not found.')
    except FileExistsError:
        a=1
        # print(f'Error: {destination_image_path} already exists.')