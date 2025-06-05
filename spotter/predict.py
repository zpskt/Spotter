import argparse
import os

from cv2.gapi.wip.draw import Image
from ultralytics import YOLO

from config import logger, PROJECT_ROOT

# 预测
def predict():
    model = YOLO('D:\\zpskt\\Spotter\\model\\smoke_and_fire.pt')
    results = model.predict(source='D:\\zpskt\\Spotter\\data\\images', imgsz=640,
                            project='D:\\zpskt\\Spotter\\runs\\detect', name='smoke', save=True, conf=0.2, iou=0.7, )
    # 检查是否检测到了目标
    detected = False
    for result in results:
        # print(result.boxes)

        print(result.boxes.cls.shape) # 目标数量
        print(result.boxes.conf)
    logger.info(f"Detected: {detected}")
    return detected


if __name__ == '__main__':
    predict()
