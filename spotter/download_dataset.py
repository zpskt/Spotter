import os
import shutil

import kagglehub

from config import logger, PLATFORM_SYSTEM

from config import PROJECT_ROOT


def move_all_files(src_dir, dst_dir):
    """
    将源目录中的所有文件和子目录递归地移动到目标目录。
    :param src_dir: 源目录
    :param dst_dir: 目标目录
    :return:
    """
    logger.info(f"Moving all kaggle dataset from {src_dir} to {dst_dir}")
    # 确保目标目录存在
    os.makedirs(dst_dir, exist_ok=True)
    # 遍历源目录及其子目录
    for root, dirs, files in os.walk(src_dir):
        # 计算目标目录的相对路径
        relative_path = os.path.relpath(root, src_dir)
        target_dir = os.path.join(dst_dir, relative_path)
        os.makedirs(target_dir, exist_ok=True)
        # 移动文件
        for filename in files:
            src_file = os.path.join(root, filename)
            dst_file = os.path.join(target_dir, filename)
            shutil.move(src_file, dst_file)

        # 移动子目录（shutil.move 会自动处理子目录）
        for dir_name in dirs:
            src_subdir = os.path.join(root, dir_name)
            dst_subdir = os.path.join(target_dir, dir_name)
            shutil.move(src_subdir, dst_subdir)
    logger.info(f"Moving all kaggle dataset from {src_dir} to {dst_dir} finished")


def download_smoke_fire_dataset(dataset_name="sayedgamal99/smoke-fire-detection-yolo", dir_1="dataset", dir_2="smoke"):
    """
    download dataset from kaggle
    :param dataset_name:
    :param download_dir:
    :return: download_dir
    """
    dataset_path = os.path.join(dir_1, dir_2)
    download_dir = kagglehub.dataset_download(dataset_name)

    move_all_files(download_dir, os.path.join(download_dir, os.path.join(PROJECT_ROOT, dataset_path)))

    data_yaml_dir = os.path.join(PROJECT_ROOT, dataset_path, "data.yaml")

    #  todo 根据系统的不同，将当前的系统路径写入data.yaml中
    # 自定义前五行数据
    path = os.path.join(PROJECT_ROOT, dataset_path)
    if PLATFORM_SYSTEM == "Windows":
        lines_to_add = [
            "path: " + path + "\n",
            "train: data\\train\\images\n",
            "val: data\\val\\images\n",
            "test: data\\test\\images\n"
        ]
    else:
        lines_to_add = [
            "path: " + path + "\n",
            "train: data/train/images\n",
            "val: data/val/images\n",
            "test: data/test/images\n"
        ]

    with open(data_yaml_dir, "r") as target_file:
        # 获取目标文件现有的内容
        existing_lines = target_file.readlines()
        # 替换前五行
        new_lines = lines_to_add + existing_lines[5:]

    with open(data_yaml_dir, "w") as target_file:
        # 写入新的内容
        target_file.writelines(new_lines)


    # 删除压缩包
    os.remove(download_dir)

if __name__ == '__main__':
    try:
        download_smoke_fire_dataset()
    except Exception as e:
        print(e)
