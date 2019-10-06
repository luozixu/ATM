'''操作所有的日志工作'''
import  logging
from conf import  settings


def logger(log_type):
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOGIN_LEVEL)

    # 创建文件对象，给文件对象设置等级
    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOGIN_TYPE[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOGIN_LEVEL)

    # 设置输出对象格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 把格式添加到配置中
    fh.setFormatter(formatter)

    # 把日志打印到指定的handler
    logger.addHandler(fh)

    return logger