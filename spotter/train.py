import argparse
import os

from ultralytics import YOLO

from config import logger


def train_method_one():
    '''
    train yolo model
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
    opts = parser.parse_args()

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
    # execute yolo train
    logger.info("Starting training...")
    return_code = os.system(yolo_train_cmd)
    # check return code
    if return_code == 0:
        logger.info("yolo training completed successfully. the model is saved in runs/detect/{name}/weights/best.pt")
    else:
        logger.error("yolo training failed.")

def train_method_two():
    model = YOLO('model/yolo11n.pt')
    model.train(data='dataset/smoke/data.yaml',
                cache=False,
                imgsz=640,
                epochs=200,
                batch=16,
                close_mosaic=10,
                device='0',
                optimizer='SGD', # using SGD
                project='runs/train-obb',
                name='smoke',
                )