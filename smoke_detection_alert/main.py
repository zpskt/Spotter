from pathlib import Path

import cv2
import time

import yaml

from detection.detector import SmokeDetector
from alert.sms_notifier import SMSNotifier
from storage.image_saver import ImageSaver
from storage.logger import Logger
from utils.helpers import get_timestamp

# 加载配置文件
CONFIG_PATH = Path(__file__).parent / "config" / "settings.yaml"
with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
    CONFIG = yaml.safe_load(f)

def main():
    # 初始化各模块
    detector = SmokeDetector(model_path='detection/models/smoke_and_fire.pt')
    # notifier = SMSNotifier()
    image_saver = ImageSaver(save_dir=CONFIG['save_dir'])
    logger = Logger(log_file=CONFIG['log_file'])

    # 打开视频流
    cap = cv2.VideoCapture(CONFIG['video_source'])
    if not cap.isOpened():
        raise ValueError("无法打开视频流")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # 烟雾检测
            results = detector.detect(frame)
            # 绘制检测框并保存图像帧

            if results and results.get('smoke'):
                timestamp = get_timestamp()
                log_message = f"[{timestamp}] 检测到烟雾"

                # 保存图像
                if CONFIG['image_save_enabled']:
                    frame_with_boxes = detector.draw_detections(frame, results['smoke'])
                    image_path = image_saver.save_image(frame_with_boxes, timestamp)
                    log_message += f", 图像已保存至 {image_path}"

                # 发送短信通知
                # if CONFIG['sms_enabled']:
                #     notifier.send_alert(message=log_message)

                # 记录日志
                if CONFIG['log_enabled']:
                    logger.log(log_message)

            # 显示视频流（可选）
            cv2.imshow('Smoke Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # 控制帧率（避免过高的CPU占用）
            time.sleep(0.05)

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
