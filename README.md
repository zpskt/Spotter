# Spotter

这是一个基于深度学习的特定物体检测系统，能够训练自定义物体并在视频流中进行实时检测。

## 项目架构

## 功能特性

- 支持自定义物体训练
- 实时视频流物体检测
- 高精度识别
- 跨平台支持

## 技术栈

核心使用yolov11作为深度学习模型
官网地址：https://github.com/ultralytics
使用文档： https://docs.ultralytics.com/zh

## 环境

- Python 3.12.9
  请确保你已经安装了requirements.txt文件中列出的依赖项。

## 如何开始

· 设置国内镜像源

```shell
pip config set install.trusted-host mirrors.aliyun.com
```

安装依赖

```shell
pip install -r requirements.txt
```

ps: 关于cuda相关的的版本对应关系：https://download.pytorch.org/whl/torch_stable.html

```shell
pip install torchvision==0.18.1+cu121 -f https://download.pytorch.org/whl/torch_stable.html
```

下载Yolo11模型

```shell
mkdir -p model && cd model
wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11l.pt
```

运行程序

```shell
cd ..
python run.py
```

### 根据数据训练特定模型

使用spotter.train.py进行训练

### 使用自定义模型进行检测


### 标注图片

安装依赖

```shell
pip install labelimg
```

图片打标签

```shell
labelimg
```

查看GPU使用率

```shell
nvidia-smi
```
### 未来要做
1. 添加更多模型支持，如YOLOv8等。
2. 实现QT界面进行训练和检测。
3. 添加更多功能，如视频流处理、物体跟踪等。
   