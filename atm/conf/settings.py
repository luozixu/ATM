import  os
import  logging
import  sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #找到路径


DATABASE = {
    'engine': 'file_storage',  # support mysql,postgresql in the future
    'name': 'accounts',
    'path': "%s/db" % BASE_DIR
}

# 日志类型
LOGIN_LEVEL = logging.INFO
LOGIN_TYPE = {
    "transaction": "transactions.log",
    "access": "access.log",
}


# 用户交易类型，每个类型对应一个字典，包括帐户金额变动方式，利息
TRANSACTION_TYPE = {
    'repay':{'action':'plus','interest':0},
    'withdraw':{'action':'minus','interest':0.05},
    'transfer':{'action':'minus','interest':0.05},
    'consume':{'action':'minus','interest':0},
}

