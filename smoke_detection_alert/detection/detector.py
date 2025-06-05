import cv2
import torch
import numpy as np
from ultralytics import YOLO


class SmokeDetector:
    def __init__(self, model_path='models/smoke_model.pt'):
        """
        初始化烟雾检测器
        :param model_path: YOLOv5 模型路径
        """
        # 加载 yolo11l 模型（支持本地 .pt 文件或在线模型）
        # self.model = torch.hub.load('models/yolo11l.pt', 'smoke', path=model_path)
        self.model = YOLO(model_path)


    def detect(self, frame):
        """
        在给定的图像帧中执行烟雾检测
        :param frame: 输入图像帧 (numpy array)
        :return: 包含检测结果的字典，例如 {'smoke': [(x1, y1, x2, y2), ...]}
        """
        # 执行推理
        # results = self.model.predict(frame, imgsz=640,
        #                         project='D:\\zpskt\\Spotter\\runs\\detect', name='smoke', save=True, conf=0.2, iou=0.7)
        results = self.model(frame)

        # 解析结果

        smoke_boxes = []

        # 解析第一个结果（因为只传入了一帧图像）
        for result in results:
            boxes = result.boxes  # Boxes 对象，包含所有检测框
            for box in boxes:
                cls = int(box.cls)  # 类别索引
                label = result.names[cls]  # 类别名称（如 'smoke'）
                conf = float(box.conf)  # 置信度
                if label == 'smoke' and conf >= 0.6:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])  # 获取边界框坐标
                    smoke_boxes.append((x1, y1, x2, y2))

        return {'smoke': smoke_boxes}

    def draw_detections(self, frame, detection_result):
        """
        在图像上绘制检测框
        :param frame: 输入图像帧 (numpy array)
        :param detection_result: detect 方法返回的结果
        :return: 绘制后的图像帧
        """

        if isinstance(detection_result, dict):
            smoke_boxes = detection_result.get('smoke', [])
        else:
            smoke_boxes = []
        print(f"[DEBUG] 检测到 {len(smoke_boxes)} 个烟雾区域")  # 添加在 draw_detections 函数中
        for box in smoke_boxes:
            x1, y1, x2, y2 = box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 红色矩形框
            cv2.putText(frame, 'Smoke', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        return frame
