# storage/image_saver.py

import os
import cv2
from datetime import datetime


class ImageSaver:
    def __init__(self, save_dir='./detected_images'):
        """
        初始化图像保存工具
        :param save_dir: 图像保存的目录
        """
        self.save_dir = save_dir
        os.makedirs(self.save_dir, exist_ok=True)  # 如果目录不存在则创建

    def save_image(self, image, timestamp=None, prefix='smoke'):
        """
        保存图像帧到指定目录
        :param image: 要保存的图像帧 (numpy array)
        :param timestamp: 时间戳（可选），格式为字符串或 datetime 对象
        :param prefix: 文件名前缀，默认为 'smoke'
        :return: 保存后的图像路径
        """
        if timestamp is None:
            timestamp = datetime.now()
        elif isinstance(timestamp, str):
            try:
                timestamp = datetime.strptime(timestamp, "%Y%m%d_%H%M%S")
            except ValueError:
                timestamp = datetime.now()

        # 构建文件名
        timestamp_str = timestamp.strftime("%Y%m%d_%H%M%S")
        filename = f"{prefix}_{timestamp_str}.jpg"
        file_path = os.path.join(self.save_dir, filename)

        # 保存图像
        cv2.imwrite(file_path, image)
        return file_path
