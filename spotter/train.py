import argparse
import os

from ultralytics import YOLO

from config import logger


def train_via_cli(opts):
    '''
    使用yolo脚本命令训练模型
    :param opts:
    :return:
    '''
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
    # opts = parser.parse_args()

    yolo_train_cmd = (
            "yolo train"
            + " data="
            + opts.data
            + " model="
            + opts.model
            + " name="
            + opts.name
            + " epochs="
            + str(opts.epochs)
            + " imgsz="
            + str(opts.imgsz)
            + " batch="
            + str(opts.batch)
            + " workers="
            + str(opts.workers)
            + " device="
            + opts.device
    )
    logger.info("Starting training...")
    # 使用系统命令行训练
    return_code = os.system(yolo_train_cmd)
    # check return code
    if return_code == 0:
        logger.info("yolo training completed successfully. the model is saved in runs/detect/{name}/weights/best.pt")
    else:
        logger.error("yolo training failed.")

def train_via_api(opts):
    """
    Train model using YOLO's Python API.
    :param opts: Parsed command-line options.
    """
    model = YOLO(opts.model)
    model.train(
        data=opts.data,
        imgsz=opts.imgsz,
        epochs=opts.epochs,
        batch=opts.batch,
        device=opts.device,
        project='runs/train',
        name=opts.name,
        cache=False,
        close_mosaic=10,
        optimizer='SGD'
    )

def train(opts):
   """
   Unified training entry point.
   :param opts: Parsed arguments from argparse.
   """
   # 可根据需求选择不同训练方法
   train_via_cli(opts)
   # train_via_api(opts)