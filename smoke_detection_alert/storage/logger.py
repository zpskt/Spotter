# storage/logger.py

import os
import sqlite3
import logging
from datetime import datetime


class Logger:
    def __init__(self, log_file='./logs/smoke_detection.log', db_file=None, use_file=True, use_db=False):
        """
        初始化日志记录器
        :param log_file: 日志文件路径
        :param db_file: 数据库文件路径（SQLite）
        :param use_file: 是否启用文件日志记录
        :param use_db: 是否启用数据库日志记录
        """
        self.use_file = use_file
        self.use_db = use_db

        # 初始化日志文件
        self.log_file = log_file
        if self.use_file:
            os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s [%(levelname)s]: %(message)s',
                handlers=[
                    logging.FileHandler(self.log_file, encoding='utf-8'),
                    logging.StreamHandler()  # 控制台同步输出
                ]
            )

        # 初始化数据库连接
        self.conn = None
        if self.use_db:
            self.db_file = db_file or './logs/smoke_log.db'
            self._init_db()

    def _init_db(self):
        """初始化数据库及日志表"""
        self.conn = sqlite3.connect(self.db_file)
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS smoke_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    message TEXT NOT NULL
                )
            ''')

    def log(self, message):
        """
        记录日志信息
        :param message: 要记录的信息
        """
        if self.use_file:
            logging.info(message)

        if self.use_db:
            try:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.conn.execute(
                    "INSERT INTO smoke_logs (timestamp, message) VALUES (?, ?)",
                    (timestamp, message)
                )
                self.conn.commit()
            except Exception as e:
                print(f"[ERROR] 写入数据库失败：{str(e)}")

    def close(self):
        """关闭数据库连接"""
        if self.conn:
            self.conn.close()

    def __del__(self):
        self.close()
