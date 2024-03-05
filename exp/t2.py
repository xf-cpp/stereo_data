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
def autoAction(client):
# 创建深度图像捕获设置
# depth_cam = airsim.ImageCaptureBase()
# depth_cam.set_image_type(airsim.ImageType.DepthVis)
# depth_cam.set_resolution(640, 480)  # 设置分辨率，根据需要调整


    #设置到指定位置
    x_pos = -600
    y_pos = -50
    z_pos = -80
    pose = airsim.Pose(airsim.Vector3r(x_pos,y_pos,z_pos),airsim.to_quaternion(0,0,0))
    client.simSetVehiclePose(pose, True)
    #悬浮
    client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
    client.hoverAsync().join()
    # 开始录制数据
    client.startRecording()
    #往前跑五秒
    # client.moveByVelocityBodyFrameAsync(vx=10, vy=0,vz= 0, duration=5).join()
    # 停止录制数据
    client.stopRecording()



    # path = [airsim.Vector3r(x_pos,y_pos+200,z_pos),
    #         airsim.Vector3r(x_pos + 200, y_pos+200, z_pos),
    #         airsim.Vector3r(x_pos+200, y_pos, z_pos),
    #         airsim.Vector3r(x_pos, y_pos, 0)
    #         ]；；
    # client.moveOnPathAsync(path,
    #                        12, 120,
    #                        airsim.DrivetrainType.ForwardOnly, airsim.YawMode(False, 0), 20, 1).join()
    #悬浮
    # client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
    # client.hoverAsync().join()

    # # 停止录制数据
    # client.stopRecording()

if __name__ == "__main__":
    client = initAirsim()

    autoAction(client)