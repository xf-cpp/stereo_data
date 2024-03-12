import airsim
import time
import numpy as np
from PIL import Image
from scipy.interpolate import CubicSpline
from airsim import MultirotorClient, Vector3r, YawMode, Pose
def shot(client):
    client.startRecording()
    # 往前跑五秒
    # client.moveByVelocityBodyFrameAsync(vx=10, vy=0,vz= 0, duration=5).join()
    # 停止录制数据
    client.stopRecording()
def printfp(camera_name,fov,pose):
    print(f"{camera_name}'s fov:{fov}")
    print(f"{camera_name}'s pose:{pose}")
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
def initAirsim():
    # 创建AirSim客户端
    client = airsim.MultirotorClient()
    # 连接到AirSim仿真环境
    client.confirmConnection()
    client.enableApiControl(True)
    # 上电
    client.armDisarm(True)
    return client
def autoAction(client):
# 创建深度图像捕获设置
# depth_cam = airsim.ImageCaptureBase()
# depth_cam.set_image_type(airsim.ImageType.DepthVis)
# depth_cam.set_resolution(640, 480)  # 设置分辨率，根据需要调整
    cameral_name = "front_left"
    camerar_name = "front_right"
    #设置到指定位置
    x_pos = -600
    y_pos = -50.25
    z_pos = -80
    pose = airsim.Pose(airsim.Vector3r(x_pos,y_pos,z_pos),airsim.to_quaternion(0,0,0))
    client.simSetVehiclePose(pose, True)
    client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
    client.hoverAsync().join()

    #设置相机原点位置
    #当相机为前置 双目相机时 设置仰角80.1为正下 80.5略微朝前
    camera_lpose = airsim.Pose(airsim.Vector3r(x_val=0.5,y_val=0,z_val=0),airsim.to_quaternion(80.5,0,0))
    camera_rpose = airsim.Pose(airsim.Vector3r(-0.5,0,0),airsim.to_quaternion(80.5,0,0))
    client.simSetCameraPose(cameral_name, camera_lpose)
    client.simSetCameraPose(camerar_name, camera_rpose)
    # 录制一帧数据
    shot(client)



if __name__ == "__main__":
    client = initAirsim()

    autoAction(client)