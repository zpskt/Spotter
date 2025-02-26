import logging

from spotter import Spotter
# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    try:
        # 实例化Spotter类
        spotter = Spotter()
        spotter.detect()
    except Exception as e:
        logging.error(f"Main program error: {e}")
