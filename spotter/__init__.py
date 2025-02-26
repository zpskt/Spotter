# spotter/__init__.py
import cv2
from ultralytics import YOLO

class Spotter:
    def __init__(self, model_path='model/yolo11l.pt'):
        # 加载YOLO模型，默认路径为'model/yolo11l.pt'
        self.model = YOLO(model_path)
        # 初始化摄像头，0表示使用默认摄像头
        self.cap = cv2.VideoCapture(0)

    def detect(self):
        # 持续检测循环，只要摄像头处于打开状态
        while self.cap.isOpened():
            # 从摄像头读取一帧图像
            ret, frame = self.cap.read()
            # 如果读取失败则退出循环
            if not ret:
                break
            # 使用YOLO模型进行物体检测
            results = self.model(frame)
            # 在原始帧上绘制检测结果
            annotated_frame = results[0].plot()

            # 显示带有检测结果的帧
            cv2.imshow('Spotter', annotated_frame)
            # 同时显示原始帧用于对比
            cv2.imshow('Spotter Original frame', frame)

            # 检测是否按下'q'键，如果是则退出循环
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # 释放摄像头资源
        self.cap.release()
        # 关闭所有OpenCV窗口
        cv2.destroyAllWindows()

