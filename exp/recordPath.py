import airsim
import time
import numpy as np
from PIL import Image
from scipy.interpolate import CubicSpline
from airsim import MultirotorClient, Vector3r, YawMode, Pose


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


def autoAction(client,x,y,z):
    """
    设置初始相对位置 录制双目相机数据  地图坐标轴西向为Y正，南向为X正，地面向下为Z正，坐标单位为m
    初始位置，x,y,z
    第一个初始位置为底部的后置相机 坐标 -600，-50，-80
    第二个初始位置为底部的前置相机 坐标-600，-50.25，-80

    """
    cameral_name = "front_left"
    camerar_name = "front_right"
    # 设置到指定位置
    x_pos = x
    y_pos = y
    z_pos = z
    pose = airsim.Pose(airsim.Vector3r(x_pos, y_pos, z_pos), airsim.to_quaternion(0, 0, 0))
    client.simSetVehiclePose(pose, True)
    # 悬浮
    client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
    client.hoverAsync().join()

    camera_lpose = airsim.Pose(airsim.Vector3r(x_val=0.5,y_val=0,z_val=0),airsim.to_quaternion(80.5,0,0))
    camera_rpose = airsim.Pose(airsim.Vector3r(-0.5,0,0),airsim.to_quaternion(80.5,0,0))
    client.simSetCameraPose(cameral_name, camera_lpose)
    client.simSetCameraPose(camerar_name, camera_rpose)
    # 开始录制数据
    client.startRecording()

    path = [airsim.Vector3r(x_pos,y_pos+200,z_pos),
            airsim.Vector3r(x_pos + 200, y_pos+200, z_pos),
            airsim.Vector3r(x_pos+200, y_pos, z_pos),
            airsim.Vector3r(x_pos, y_pos, 0)
            ]
    client.moveOnPathAsync(path,
                           velocity=12, timeout_sec=120,
                           drivetrain=airsim.DrivetrainType.ForwardOnly,yaw_mode= airsim.YawMode(False, 0), lookahead = 20, adaptive_lookahead=1).join()
    # 悬浮
    client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
    client.hoverAsync().join()
    # # 停止录制数据
    client.stopRecording()



if __name__ == "__main__":
    client = initAirsim()
    # 第一个初始位置为底部的后置相机 坐标 -600，-50，-80
    autoAction(client, -600,-50,-80 )
    # 第二个初始位置为底部的前置相机 坐标-600，-50.25，-80
    autoAction(client,-600,-50.25,-80)
