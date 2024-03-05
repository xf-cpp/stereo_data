import os
# 读取.txt文件
txt_file_path = r'C:\Users\Administrator\Documents\AirSim\2024-01-18-17-34-57\airsim_rec.txt'
with open(txt_file_path, 'r') as file:
    lines = file.readlines()

image_folder_path = r'C:\Users\Administrator\Documents\AirSim\2024-01-18-17-34-57\mav0\cam0\test'
# 获取文件夹中的所有文件名
all_files = os.listdir(image_folder_path)
print(all_files)
# 遍历每一行，提取第二列的数字，并重命名对应的图片文件
for line in lines:
    # 假设每行由空格或制表符分隔
    columns = line.split()
    '''
    取出原始
    '''
    i = 0
    # 获取第二列的数字
    second_column = columns[1]
    if(second_column == 'TimeStamp'):
        continue
    # 构建对应的图片文件名
    image_file_name = f'{second_column}.png'  # 这里可以根据实际情况修改文件名的格式

    # 获取图片文件的原始路径
    original_image_path = r'C:\Users\Administrator\Documents\AirSim\2024-01-18-17-34-57\mav0\cam0\test/' + all_files[i]
    # 修改为你的原始图片文件夹的路径
    if(i<= len(all_files)-1):
        i= i+1
    # 获取图片文件的新路径
    new_image_path = r'C:\Users\Administrator\Documents\AirSim\2024-01-18-17-34-57\mav0\cam0\test2/' + image_file_name  # 修改为你想要保存的目标文件夹的路径

    # 重命名图片文件
    try:
        os.rename(original_image_path, new_image_path)
        print(f'Renamed {original_image_path} to {new_image_path}')
    except FileNotFoundError:
        print(f'Error: {original_image_path} not found.')