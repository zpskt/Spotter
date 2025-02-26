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
## 环境
  - Python 3.12.9
  请确保你已经安装了requirements.txt文件中列出的依赖项。
## 如何开始

1. 下载Yolo11模型
```shell
mkdir -p model && cd model
wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11l.pt
```