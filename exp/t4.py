import airsim
import time
import numpy as np
from PIL import Image
from scipy.interpolate import CubicSpline

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

    # 开始录制数据
    # client.startRecording()
    #设置到指定位置
    pose = airsim.Pose(airsim.Vector3r(0,0,-150),airsim.to_quaternion(0,0,0))
    client.simSetVehiclePose(pose, True)
    #悬浮
    # client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
    client.hoverAsync().join()
    #往前飞
    # client.moveByVelocityBodyFrameAsync(30, 0, 0, 3).join()
    # client.moveByVelocityZAsync(2, 0, -150, 3).join()
    # client.moveByVelocityZBodyFrameAsync(
    # vx = 0,
    # vy = 30,
    # z  = -150,
    # duration = 10,
    # yaw_mode = airsim.YawMode(is_rate=True, yaw_or_rate=0)
    # ).join()
    # client.moveToPositionAsync(200,0,-150,10).join()
    # 悬停
    client.hoverAsync().join()


    client.moveToPositionAsync(200, 200, -150, 10).join()
    # 悬停
    client.hoverAsync().join()


    client.moveToPositionAsync(0, 200, -150, 10).join()
    # 悬停
    client.hoverAsync().join()

    client.moveToPositionAsync(0, 0, -150, 10).join()
    # 悬停
    client.hoverAsync().join()


    client.moveToPositionAsync(-200, 0, -150, 10).join()
    # 悬停
    client.hoverAsync().join()


    client.moveToPositionAsync(-200, -200, -150, 10).join()
    # 悬停
    client.hoverAsync().join()


    client.moveToPositionAsync(0, -200, -150, 10).join()
    # 悬停
    client.hoverAsync().join()

    client.moveToPositionAsync(0,0, -150, 10).join()
    # 悬停
    client.hoverAsync().join()

# #左移
    # client.moveByVelocityZAsync(0,-5,-150,3).join()
    # # 悬停
    # client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
    # client.hoverAsync().join()
    # #往前飞
    # client.moveByVelocityZAsync(30, 0, -150, 3).join()
    # # 悬停
    # client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
    # client.hoverAsync().join()
    # # 右转
    # client.rotateByYawRateAsync(15, 6).join()
    # # 悬停
    # client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
    # client.hoverAsync().join()
    # #往前飞
    # client.moveByVelocityZAsync(40, 0, -150, 10).join()
    # # 悬停
    # client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
    # client.hoverAsync().join()
    # # 右转
    # client.rotateByYawRateAsync(15, 12).join()
    # # 悬停
    # client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
    # client.hoverAsync().join()
    # #往前飞
    # client.moveByVelocityZAsync(40, 0, -150, 10).join()
    # # 悬停
    # client.moveByVelocityBodyFrameAsync(0, 0, 0, 1).join()
    # client.hoverAsync().join()
    # 停止录制数据
    # client.stopRecording()
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

# 运行仿真或执行其他操作
# for i in range(100):
#     # 获取深度图像
#     responses = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.DepthVis, True, False)])
#     depth_image = responses[0]
#
#     # 将深度图像数据转换为NumPy数组
#     depth_data = np.array(depth_image.image_data_float, dtype=np.float32)
#     depth_data = depth_data.reshape(depth_image.height, depth_image.width)
#
#     # 在这里可以对深度图像进行进一步处理，例如保存到文件或显示
#     depth_image_pil = Image.fromarray((depth_data * 255).astype(np.uint8))
#     # depth_image_pil.show()
#
#     time.sleep(0.1)



# 获取录制的数据文件路径
# recording_path = client.getRecordingFileFullPath()

# 输出录制的数据文件路径
# print(f"Recording saved to: {recording_path}")


if __name__ == "__main__":
    client = initAirsim()
    total_time = 30

    time_step = 0.1  # 时间步长
        # 创建时间数组
    time_points = np.arange(0, total_time, time_step)

    # 初始化变量
    target_velocity = np.zeros_like(time_points)

    getSpeed()

    autoAction(client)