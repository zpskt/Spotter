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

## 前置条件

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
## 示例使用 
运行程序后，会默认下载kaggle烟雾图片数据集，并利用Yolo11的模型对其进行训练，
针对于烟雾识别的模型将会存储至runs/detect/{mode_name}/weights/best.pt 
然后就可以运行视频流进行检测

```shell
cd ..
python run.py
```

### 定制化训练模型
定制化训练一共分为以下几个步骤：
1、 准备预训练模型
2、 准备数据集（定制化一般都没有现成的数据集，需要自己打标签制作了）
3、 训练模型（生成pt）
4、 测试模型
#### 1、 准备预训练模型
我这里是下载yolo11，可以根据需求不同使用不同的预加载模型
```shell
mkdir -p model && cd model
wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11l.pt
```
#### 2、 准备数据集
我是用的labelimg进行图片标注

安装依赖

```shell
pip install labelimg
```

图片打标签

```shell
labelimg
```
#### 3、 训练模型
训练方法位于spotter/train.py中，里面有两个方法，可以根据需求传参并选择对应方法训练。

#### 4、 测试模型
测试方法位于spotter/val.py中，根据模型路径去测试模型效果

####  5、 使用模型

测试方法位于spotter/predict.py中，只是一个简单示例。


### 其他
查看GPU使用率

```shell
nvidia-smi
```
### 未来要做
1. 添加更多模型支持，如YOLOv8等。
2. 实现QT界面进行训练和检测。
3. 添加更多功能，如视频流处理、物体跟踪等。
   