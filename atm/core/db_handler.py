#处理与数据库的交互，若是file_db_storage,返回路径
import  json
import  time
from conf import  settings

def file_db_handle(conn_params):
    '''
    parse the db file path  对文件路径做语法分析
    :param conn_params:
    :return:
    '''

    db_path = "%s/%s"% (conn_params["path"], conn_params["name"])
    print('db_handler',db_path)
    return db_path

def db_handle(conn_parms):
    '''
    :param conn_parms: the db connection params set in settings
    :return: a
    DATABASE = {
    'engine':'file_storage',       #文件存储，这里可扩展成数据库形式的
    'name':'accounts',              #db下的文件名
    'path':'%s/db' %BASE_DIR
}
    '''

    if conn_parms["engine"] == "file_storage":
        return  file_db_handle(conn_parms)
