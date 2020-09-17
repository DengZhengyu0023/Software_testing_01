"""
    获取日志器
"""

# 导包
import logging.handlers

class GetLogger:

    logger = None
    @classmethod
    def get_logger(cls):
        if not cls.logger:
            # 获取日志器
            cls.logger = logging.getLogger("admin")
            # 设置日志器级别
            cls.logger.setLevel(logging.INFO)

            # 获得处理器
                # 控制台处理器
            sh = logging.StreamHandler()
                # 保存文件日志处理器 时间
            th = logging.handlers.TimedRotatingFileHandler(filename="../log/Tpshop.log",
                                                           when="S",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf_8")
            # 设置th处理器级别
            th.setLevel(logging.ERROR)

            # 获得格式器
            format = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(format)

            # 设置处理器格式
            sh.setFormatter(fm)
            th.setFormatter(fm)

            # 日志器添加处理器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)

        # 返回日志器
        return cls.logger