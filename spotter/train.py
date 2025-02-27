import os

from config import logger


def train(opts):
    '''
    train yolo model
    :param opts:
    :return:
    '''
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