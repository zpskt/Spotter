# utils/helpers.py

import os
from datetime import datetime
import logging


def get_timestamp(fmt="%Y%m%d_%H%M%S"):
    """
    获取当前时间戳字符串
    :param fmt: 时间格式，默认为 'YYYYMMDD_HHMMSS'
    :return: 格式化后的时间字符串
    """
    return datetime.now().strftime(fmt)


def create_dir_if_not_exists(path):
    """
    如果目录不存在则创建
    :param path: 目录路径
    :return: 创建后的目录路径
    """
    os.makedirs(path, exist_ok=True)
    return path


def setup_logger(log_file=None, level=logging.INFO):
    """
    配置全局日志记录器
    :param log_file: 日志文件路径（可选）
    :param level: 日志级别
    """
    logging.basicConfig(level=level, format='%(asctime)s [%(levelname)s]: %(message)s')

    if log_file:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s'))
        logging.getLogger().addHandler(file_handler)


def get_relative_path(base_path, *paths):
    """
    获取相对路径
    :param base_path: 基础路径
    :param paths: 要拼接的路径片段
    :return: 拼接后的完整路径
    """
    return os.path.join(base_path, *paths)


def is_valid_image_extension(filename):
    """
    判断文件是否是图像格式
    :param filename: 文件名或路径
    :return: bool
    """
    valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    ext = os.path.splitext(filename)[1].lower()
    return ext in valid_extensions


def format_seconds_to_hms(seconds):
    """
    将秒数转换为小时、分钟、秒格式
    :param seconds: 秒数
    :return: 字符串如 '01h 23m 45s'
    """
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}h {m:02d}m {s:02d}s"
