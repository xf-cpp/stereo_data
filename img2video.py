import cv2
import os
from tqdm import tqdm
# 图像帧的文件夹路径
# frames_folder = r'C:\Users\Administrator\Documents\AirSim\2024-03-05-14-42-26\images'
frames_folder = r'C:\Users\Administrator\Documents\AirSim\2024-03-11-18-05-46\images\right'

# 获取图像帧文件列表
frame_files = sorted([f for f in os.listdir(frames_folder) if f.endswith('.png')])

# 设置输出视频文件的名称、编码器、帧率和帧大小
output_video_file = 'right311.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 20
frame_size = (640, 480)

# 创建 VideoWriter 对象
video_writer = cv2.VideoWriter(output_video_file, fourcc, fps, frame_size)
data_bar = tqdm(frame_files,desc="Processing")
# 逐帧读取图像并写入视频

for frame_file in frame_files:

    frame_path = os.path.join(frames_folder, frame_file)
    frame = cv2.imread(frame_path)

    # 如果图像大小与设置的帧大小不同，调整图像大小
    if frame.shape[:2] != frame_size:
        frame = cv2.resize(frame, frame_size)
    # 将帧写入视频文件
    video_writer.write(frame)
    data_bar.update()
# for frame_file in frame_files:
#
#     frame_path = os.path.join(frames_folder, frame_file)
#     frame = cv2.imread(frame_path)
#
#     # 如果图像大小与设置的帧大小不同，调整图像大小
#     if frame.shape[:2] != frame_size:
#         frame = cv2.resize(frame, frame_size)
#
#     # 将帧写入视频文件
#     video_writer.write(frame)

# 关闭 VideoWriter 对象
video_writer.release()

print(f"Video generated and saved to {output_video_file}")
