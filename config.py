# 定义全局变量存储项目根目录
import logging
import os
import platform

# 当前项目根目录
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# 当前系统类型
PLATFORM_SYSTEM = platform.system()

# 创建logs目录
os.makedirs('logs', exist_ok=True)

# 基础日志配置
logging.basicConfig(
    level=logging.INFO,  # 设置日志记录级别为INFO，即只记录INFO及以上级别的日志
    format='%(asctime)s - %(levelname)s - %(message)s',  # 定义日志格式：时间 - 日志级别 - 日志信息
    filename=os.path.join(PROJECT_ROOT, "logs","spotter.log"),  # 指定日志文件路径，位于项目根目录下的logs文件夹中
    filemode='a'  # 设置文件模式为追加模式（'a'），即每次运行程序时日志会追加到文件末尾，而不是覆盖
)

# 获取根日志记录器
logger = logging.getLogger()
