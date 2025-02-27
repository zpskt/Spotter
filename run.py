import argparse
import os
import platform

import torch

from config import logger
from spotter.download_dataset import download_smoke_fire_dataset
from spotter.train import train

# 定义全局变量存储项目根目录
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# 入参提取


def run():


    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="model/yolo11l.pt", help="Path to the model file")
    parser.add_argument("--data", type=str, default="dataset/smoke/data.yaml", help="Path to the yolo train data file")
    parser.add_argument("--epochs", type=int, default=2, help="Number of epochs to train the model")
    parser.add_argument("--imgsz", type=int, default=320, help="Image size for training")
    parser.add_argument("--batch", type=int, default=8, help="Batch size for training")
    parser.add_argument("--workers", type=int, default=0, help="Number of workers for training")
    parser.add_argument("--device", type=str, default="cuda", help="Device to use for training")
    parser.add_argument("--name", type=str, default="yolo11l", help="Name of the model")
    parser.add_argument("--dataset", type=bool, default=True, help="Download dataset directory")
    opts = parser.parse_args()

    # get system platform
    platform_system = platform.system()
    logger.info(f"System platform: {platform_system}")
    # define model accelerator

    if platform_system == "Darwin" and torch.backends.mps.is_available() and opts.device == "mps":
        device = "mps"
    elif torch.cuda.is_available() and opts.device == "cuda":
        device = "cuda"
    else:
        device = "cpu"
    logger.info(f"Using {device} device.")

    # spotter = Spotter()
    # spotter.detect()

    # download dataset
    if not os.path.exists("dataset/smoke/data.yaml"):
        logger.info("Dataset not found. Downloading...")
        download_smoke_fire_dataset()

    else:
        logger.info("Dataset found. Skipping download.")
    train(opts)


if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        logger.error(f"Main program error: {e}")
