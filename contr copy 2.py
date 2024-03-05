# coding=utf-8
import keyboard
import airsim
import numpy as np
import math
import threading
import cv2
import time
# import control as ctrl
# import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


# def callBackFunc(x):
#     w = keyboard.KeyboardEvent('down', 28, 'w')             # 前进
#     s = keyboard.KeyboardEvent('down', 28, 's')             # 后退
#     a = keyboard.KeyboardEvent('down', 28, 'a')             # 左移
#     d = keyboard.KeyboardEvent('down', 28, 'd')             # 右移
#     up = keyboard.KeyboardEvent('down', 28, 'up')           # 上升
#     down = keyboard.KeyboardEvent('down', 28, 'down')       # 下降
#     left = keyboard.KeyboardEvent('down', 28, 'left')       # 左转
#     right = keyboard.KeyboardEvent('down', 28, 'right')     # 右转
#     k = keyboard.KeyboardEvent('down', 28, 'k')             # 获取控制
#     l = keyboard.KeyboardEvent('down', 28, 'l')             # 释放控制

#     if x.event_type == 'down' and x.name == w.name:
#         # 前进
#         client.moveByVelocityBodyFrameAsync(6, 0, 0, 0.5)
#         # print("前进")
#     elif x.event_type == 'down' and x.name == s.name:
#         # 后退
#         client.moveByVelocityBodyFrameAsync(-6, 0, 0, 0.5)
#         # print("后退")
#     elif x.event_type == 'down' and x.name == a.name:
#         # 左移
#         client.moveByVelocityBodyFrameAsync(0, -6, 0, 0.5)
#         # print("左移")
#     elif x.event_type == 'down' and x.name == d.name:
#         # 右移
#         client.moveByVelocityBodyFrameAsync(0, 6, 0, 0.5)
#         # print("右移")
#     elif x.event_type == 'down' and x.name == up.name:
#         # 上升
#         client.moveByVelocityBodyFrameAsync(0, 0, -2, 0.5)
#         # print("上升")
#     elif x.event_type == 'down' and x.name == down.name:
#         # 下降
#         client.moveByVelocityBodyFrameAsync(0, 0, 0.5, 0.5)
#         # print("下降")
#     elif x.event_type == 'down' and x.name == left.name:
#         # 左转
#         client.rotateByYawRateAsync(-20, 0.5)
#         # print("左转")
#     elif x.event_type == 'down' and x.name == right.name:
#         # 右转
#         client.rotateByYawRateAsync(20, 0.5)
#         # print("右转")
#     elif x.event_type == 'down' and x.name == k.name:
#         # 无人机起飞
#         # get control
#         client.enableApiControl(True)
#         print("get control")
#         # unlock
#         client.armDisarm(True)
#         print("unlock")
#         # Async methods returns Future. Call join() to wait for task to complete.
#         client.takeoffAsync().join()
#         print("takeoff")
#     elif x.event_type == 'down' and x.name == l.name:
#         # 无人机降落
#         client.landAsync().join()
#         print("land")
#         # lock
#         client.armDisarm(False)
#         print("lock")
#         # release control
#         client.enableApiControl(False)
#         print("release control")
#     else:
#         # 没有按下按键
#         client.moveByVelocityBodyFrameAsync(0, 0, 0, 0.5).join()
#         client.hoverAsync().join()  # 第四阶段：悬停6秒钟
#         print("悬停")

def action(client):
    global target_velocity, time_step, response
    try:
        client.enableApiControl(True)
        # 上电
        client.armDisarm(True)

        # 开始录制
        client.startRecording()

        # 上升 10m/s 上升10s
        client.moveByVelocityBodyFrameAsync(0, 0, -10, 20).join()

        # 悬停
        client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
        client.hoverAsync().join() 

        # 前进
        # client.moveByVelocityBodyFrameAsync(10, 0, 0, 1).join()
        # # 前进
        # client.moveByVelocityBodyFrameAsync(8, 0, 0, 1).join()
        # # 前进
        # client.moveByVelocityBodyFrameAsync(6, 0, 0, 1).join()
        # # 前进
        # client.moveByVelocityBodyFrameAsync(4, 0, 0, 1).join()
        # # 前进
        # client.moveByVelocityBodyFrameAsync(2, 0, 0, 1).join()
        # # 前进
        # client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()

        # 前进
        for i, velocity in enumerate(target_velocity):
            client.moveByVelocityBodyFrameAsync(velocity, 0, 0, time_step).join()

        # 悬停
        client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
        client.hoverAsync().join() 

        # 右转
        client.rotateByYawRateAsync(15, 6).join()

        # 悬停
        client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
        client.hoverAsync().join() 

        # 前进
        for i, velocity in enumerate(target_velocity):
            client.moveByVelocityBodyFrameAsync(velocity, 0, 0, time_step).join()

        # 悬停
        client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
        client.hoverAsync().join() 

        # 右转
        client.rotateByYawRateAsync(15, 6).join()

        # 悬停
        client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
        client.hoverAsync().join() 

        # 前进
        for i, velocity in enumerate(target_velocity):
            client.moveByVelocityBodyFrameAsync(velocity, 0, 0, time_step).join()

        # 悬停
        client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
        client.hoverAsync().join() 

        # 右转
        client.rotateByYawRateAsync(15, 6).join()

        # 悬停
        client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
        client.hoverAsync().join() 

        # 前进
        for i, velocity in enumerate(target_velocity):
            client.moveByVelocityBodyFrameAsync(velocity, 0, 0, time_step).join()

        # 悬停
        client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
        client.hoverAsync().join() 

        # 右转
        client.rotateByYawRateAsync(15, 6).join()

        # 悬停
        client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
        client.hoverAsync().join() 

        # 下降 10m/s 下降10s
        client.moveByVelocityBodyFrameAsync(0, 0, 10, 20).join()

    finally:
        # 停止录制
        client.stopRecording()

        # 下电
        client.armDisarm(False)

        client.enableApiControl(False)

def get_IntrinsicMatrix(client, camera_name, vehicle_name=None):
    intrinsic_matrix = np.zeros([3, 3])
    fov = client.simGetCameraInfo(camera_name, external=False).fov
    request = [airsim.ImageRequest(camera_name, airsim.ImageType.Scene, False, False)]
    responses = client.simGetImages(request)
    img_width = responses[0].width
    img_height = responses[0].height
    intrinsic_matrix[0, 0] = img_width / 2 / math.tan(math.radians(fov / 2))
    intrinsic_matrix[1, 1] = img_width / 2 / math.tan(math.radians(fov / 2))
    intrinsic_matrix[0, 2] = img_width / 2
    intrinsic_matrix[1, 2] = img_height / 2
    intrinsic_matrix[2, 2] = 1
    return intrinsic_matrix

def getSpeed():
    global total_time, time_step, time_points, target_velocity
    # 创建系统模型
    # 初始化变量
    target_velocity = np.zeros_like(time_points)

    # 定义平滑速度曲线的控制点
    control_points = [(0, 0), (10, 10), (20, 0)]  # (时间, 速度)

    # 创建三次样条插值
    time_points_interp = np.linspace(0, total_time, 200)  # 更多的插值点以获得平滑曲线
    cs = CubicSpline(*zip(*control_points), bc_type='natural')

    # 插值得到平滑速度曲线
    target_velocity = cs(time_points_interp)

def getDepth():
    """
    获取深度图片
    img_depth_planar:
    物体到相机光心的位置
    img_depth_perspective:
    物体到相平面的距离
    :return:
    """
    request = [
     airsim.ImageRequest('front_center', airsim.ImageType.DepthPlanar, True, False),
     airsim.ImageRequest('front_center', airsim.ImageType.DepthPerspective, True, False)]
    responses = client.simGetImages(request)
    img_depth_planar = np.array(responses[0].image_data_float).reshape(responses[0].height, responses[0].width)
    # 2. 距离100米以上的像素设为白色（此距离阈值可以根据自己的需求来更改）
    img_depth_vis = img_depth_planar / 100
    img_depth_vis[img_depth_vis > 1] = 1.
    # 3. 转换为整形
    img_depth_vis = (img_depth_vis * 255).astype(np.uint8)
    # 4. 保存为文件
    cv2.imwrite('DepthVis.png', img_depth_vis)
    

if __name__ == '__main__':

    total_time = 30

    time_step = 0.1  # 时间步长
        # 创建时间数组
    time_points = np.arange(0, total_time, time_step)

    # 初始化变量
    target_velocity = np.zeros_like(time_points)

    getSpeed()

    # 建立脚本与AirSim环境的连接
    client = airsim.MultirotorClient()
    client.confirmConnection()

    # 获取所有相机名称
    # camera_names = client.simGetCameraInfo()
    # print("Available cameras:", camera_names)

    # 获取相机内参
    # camera_name = "front_center"  # 替换成你实际使用的相机名称
    camera_name = "front_left"  # 替换成你实际使用的相机名称

    # camera_info = client.simGetCameraInfo(camera_name)
    K = get_IntrinsicMatrix(client, camera_name)
    print(K)
    action(client)





