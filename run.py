import logging

from spotter import Spotter
# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    try:
        # get system platform
        platform_system = platform.system()
        logging.info(f"System platform: {platform_system}")
        # define model accelerator
        # todo: change to user to choose(cuda mps cpu )
        if platform_system == "Darwin":
            accelerator = "mps"
        else:
            accelerator = "cuda"
        # spotter = Spotter()
        # spotter.detect()
        # download dataset
        if not os.path.exists("dataset/smoke/data.yaml"):
            logging.info("Dataset not found. Downloading...")
            dataset_path = download_smoke_fire_dataset()
            logging.info(f"Dataset downloaded to: {dataset_path}")
        else:
            logging.info("Dataset found. Skipping download.")

        yolo_train_cmd = (
                "yolo train data="
                + "dataset/smoke/data.yaml "
                + "model=model/yolo11l.pt "
                + "epochs=300 imgsz=640 batch=8 workers=0 "
                + "device="
                + accelerator
        )
        # execute yolo train
        logging.info("Starting training...")
        return_code = os.system(yolo_train_cmd)
        # check return code
        if return_code == 0:
            logging.info("Training completed successfully.")
        else:
            logging.error("Training failed.")

    except Exception as e:
        logging.error(f"Main program error: {e}")
