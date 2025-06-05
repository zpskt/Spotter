## 烟雾检测报警系统

### 项目结构
smoke_detection_alert/
├── main.py                       # 系统启动入口
├── config/                       # 配置文件目录
│   ├── settings.yaml             # 主配置文件（如模型路径、摄像头地址等）
│   └── sms_config.yaml           # 短信推送相关配置
├── detection/                    # 图像检测模块
│   ├── detector.py               # 检测器类，封装视频流处理与检测逻辑
│   └── models/                   # 存放检测模型相关文件
│       └── smoke_model.pt        # 示例：YOLOv5训练好的烟雾检测模型
├── alert/                        # 报警通知模块
│   └── sms_notifier.py           # 短信通知实现类（如使用阿里云短信服务）
├── storage/                      # 数据存储模块
│   ├── image_saver.py            # 图像保存工具类
│   └── logger.py                 # 日志记录模块，支持写入数据库或日志文件
├── utils/                        # 工具类
│   └── helpers.py                # 公共辅助函数（如时间格式化、路径生成等）
└── requirements.txt              # 项目依赖库列表