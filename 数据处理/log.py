
import time
from loguru import logger
from pathlib import Path
import os

# project_path = Path.cwd().parent
# log_path = Path(project_path, "log")
# t = time.strftime("%Y_%m_%d")


class Loggings():
    __instance = None
    path = r'C:\Users\zhangbinghui\PycharmProjects\anaconda\log'
    log_path = time.strftime("%Y-%m-%d_%H_%M_%S") + ".log"
    lpath = os.path.join(path, log_path)

    logger.add(lpath, encoding='utf-8', enqueue=True, rotation='50MB', compression='zip', retention="10 days")
    # logger.add(f"{log_path}/interface_log_{t}.log", rotation="500MB", encoding="utf-8", enqueue=True,
    #            retention="10 days")

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Loggings, cls).__new__(cls, *args, **kwargs)

        return cls.__instance

    def info(msg):
        return logger.info(msg)

    def debug(self, msg):
        return logger.debug(msg)

    def warning(self, msg):
        return logger.warning(msg)

    def error(self, msg):
        return logger.error(msg)


# loggings = Loggings()
# if __name__ == '__main__':
#     loggings.info("中文test")
#     loggings.debug("中文test")
#     loggings.warning("中文test")
#     loggings.error("中文test")

    # logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature='f-strings')
    # n1 = "cool"
    # n2 = [1, 2, 3]
    # logger.info(f'If you are using Python {n1}, prefer {n2} of course!')