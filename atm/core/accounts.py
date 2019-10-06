import  os
import  sys
import  json
import  logging
import  time
import  datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import  auth
from core import  db_handler
from conf import  settings

def load_current_balance(account_id):
    '''
    # 把数据load下，返回账户余额和其他基础信息
    :param account_id: 用户账户的名字
    :return:
    '''
    db_path = db_handler.db_handle(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path, account_id)
    print('accounts', account_file)
    with open(account_file, 'r', encoding='utf-8') as f:
        acc_data = json.load(f)
        print('accounts_load_current',acc_data)
        return acc_data
def dump_account(account_dic):
    '''
    在更新完后，把数据dump到文件中,文件地址为\atm-learn/db/accounts
    :param account_dic:
    :return:
    '''
    db_path = db_handler.db_handle(settings.DATABASE)
    print('accounts',db_path)
    account_file = "%s/%s.json" % (db_path, account_dic['id'])
    print(account_file)
    with open(account_file, 'w', encoding='utf-8') as f:
        print('account_dic', account_dic)
        acc_data = json.dump(account_dic,f)
        print('write',acc_data)