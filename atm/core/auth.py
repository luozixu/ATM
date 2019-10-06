# 认证模块
import os
import  json
import time

from core import  accounts
from bin import  manae
from core import  main
from core import  db_handler
from conf import  settings

def access_auth(account, password, log_obj):
    """
         下面的access_login调用access_auth方法，用于登陆
         :param acount: 用户名
         :param password: 密码
        :return:如果未超期，返回字典，超期则打印相应提示

        """
    db_path = db_handler.db_handle(settings.DATABASE) #调用db_handle下的handle方法,返回路径/db/accounts
    print(db_path)
    account_file = "%s/%s.json" %(db_path, account) #用户文件
    print(account_file)
    if os.path.isfile(account_file):   #如果用户文件存在（即用户存在）
        with open(account_file, 'r', encoding='utf-8') as f: #打开文件
            account_data = json.load(f)   #file_data为字典形式
            print(account_data)
            if account_data['password'] == password:
                expire_time = time.mktime(time.strptime(account_data["expire_date"],'%Y-%m-%d'))
                print(expire_time)
                if time.time() > expire_time:  #如果信用卡已经过期，当前时间戳大于国企的时间戳
                    log_obj.error("Account [%s] had expired,Pleas contract the bank" % account)
                    print("\033[31;1mAccount %s had expired,Please contract the bank" %account)
                else:  #信用卡未过期，返回用户数据的字典
                    log_obj.info("Account [%s] logging success" % account)
                    return account_data
            else:
                log_obj.error("Account or Password does not correct!")
                print("\033[31;1mAccount or Passwordoes not correct!\033[0m")
    else:
        log_obj.error("Account [%s] does not exist!" % account)
        print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)

def access_login(user_data, log_obj):
   """
   用记登陆，当登陆失败超过三次则退出
   :param user_data: main.py里面的字典
   :return:若用户帐号密码正确且信用卡未超期，返回用户数据的字典
   """
   retry = 0
   while not user_data["is_authenticated"] and retry < 3:
       account = input('\033[32;1mplease input Acount:\033[0m').strip()
       password = input('\033[32;1mplease input Password:\033[0m').strip()
       # 用户账号密码正确而且信用卡未过期，返回用户数据的字典
       auth = access_auth(account, password, log_obj)
       print(auth)
       if auth:
           user_data["is_authenticated"] = True  #用户认证为True
           user_data["account_id"] = account  #用户账号ID为账号名
           return  auth
           retry +=1
       else:
           print("Account [%s] try logging too many times..." % account)
           log_obj.error("Account [%s] try logging too many times..." % account)
           exit()





