# 定义全局变量存储项目根目录
import os

from config import PROJECT_ROOT
from spotter.download_dataset import download_smoke_fire_dataset

if __name__ == '__main__':

    download_smoke_fire_dataset()