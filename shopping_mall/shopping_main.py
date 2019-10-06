import datetime
import os
import json


def auth_login():
    '''
    登陆密码账号
    :return:
    '''
    print("-------welcome to shopping_mall--------")
    username = input("\033[32;1mplease input Username：\033[0m")
    password = input("\033[32;1mplease input Password：\033[0m")
    account = account_auth(username, password)

    return account

def account_auth(username,password):
    '''
    用户认证账户信息格式化读取模块,并验证账号密码是否正确
    :return:
    '''
    username_file = '%s.json'%username
    print(username_file)
    if os.path.isfile(username_file):
        with open(username_file,'r',encoding='utf-8') as f:
            username_data = json.load(f)
            if username_data['password'] == password:
                balance = username_data['balance']
                print("\033[32;1myou balance is %s\033[0m"% balance)
                return account_shopping(username,balance)
            else:
                print("\033[31;1mAccount or Passwordoes not correct!\033[0m")


def account_shopping(username, balance):
    '''用户购物操作
    这次只能买一件东西，不能重复买
    '''
    goods = [
        {"name": "电脑", "price": 6999},
        {"name": "鼠标", "price": 300},
        {"name": "游艇", "price": 2000},
        {"name": "美女", "price": 9980},
    ]
    print("*".center(40, '*'))
    print("goods".center(40, '-'))
    for index, item in enumerate(goods):
        print(index, item)
    print('end'.center(40, '-'))
    while True:
        choice = input("请输入要想购买的商品编号(或者按q直接退出)：")
        if choice.isdigit():  # 判断是否为数字
            choice = int(choice)
            if choice >= 0 and choice < len(goods):  # 判断是否在商品范围里面
                choice_goods = goods[choice].get('name')
                print("you will buy \033[32;1m%s\033[0m" % choice_goods)
                if balance > goods[choice].get('price'):
                    new_balance = balance - goods[choice].get('price')
                    print("now your balance is \033[32;1m%s\033[0m" % new_balance)
                else:
                    print("sorry your balance is \033[32;1m%s\033[0m,unable to purchase" % balance)
                    continue
            else:
                print("\033[31;1mplease input the correct goods number\033[0m")
        elif choice == 'q':
            exit()

        return write_data(username, new_balance)


def write_data(username, new_balance):
    '''
    买了东西之后，余额信息更新一下
    :param username: 用户姓名
    :param new_balance: 余额信息
    :return:
    '''
    username_file = '%s.json' % username
    usernew_file = '%s.json' % username
    f = open(username_file, 'r', encoding='utf-8')
    username_data = json.load(f)
    username_data['balance'] = new_balance
    f.close()
    fnew = open(usernew_file, 'w', encoding='utf-8')
    new_data = json.dump(username_data, fnew)

    fnew.close()


def run_shopping():
    '''
    当程序启动的时候，调用，主要用于实现主要交互逻辑,客户认证登陆函数
    :return:
    '''
    userdata = auth_login()

def account_recharge(balance):
    '''用户充值操作,此思路是接ATM'''
    recharge_money = input("please input recharge money: ")
    recharge_money = int(recharge_money)
    balance = balance + recharge_money
    print("Congratulations. Recharge success. balance is \033[32;1m%s\033[0m" % balance)

    return balance

def legout():
    '''
    退出程序
    :return:
    '''
    print("\033[32;1m-------Looking forward to your next visit-------\033[0m")
    exit()

def interactive(acc_data):
    '''
    用户交互
    :param acc_data:
    :return:
    '''
    msg = (
        '''
        ------------------SHOPPING INFO --------------
                        \033[31;1m1.购物
                        2.充值
                        3.退回
        \033[0m'''
    )
    menu_dic = {
        "1": account_shopping,
        "2": account_recharge,
        "3": legout,

    }
    exit_flag = False
    while not exit_flag:
        print(msg)
        user_choice = input(">>>>").strip()
        if user_choice in menu_dic:
            menu_dic[user_choice]()
        else:
            print("\033[31;1mYou choice doesn't exist!\033[0m")

def manage_accountauth():
    '''
    管理员账户认证函数，
    :return:
    '''
    manage_account = []
    with open('manageinfo.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            i_space = i.replace('\n', '')
            manage_account.append(i_space)

    return manage_account

def account_balance():
    '''
    账户余额信息格式化读取模块
    :return:
    '''
    balance = []
    with open('account_balance.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            i_space = i.replace('\n', '')
            balance.append(i_space)

    return balance

def account_save(account, cash):
    '''
    把账户及其余额信息持久化到本地，以消除文件内容，然后以读写的方式打开文件
    :param account: 用户信息
    :return:
    '''
    save_info = open('account_balance.txt', 'w+', encoding='utf-8')
    save_info.write(account)
    save_info.write('\n')
    save_info.write(str(cash))
    save_info.close()

def account_auth_changshi(username, password):
    '''
    用户认证账户信息格式化读取模块,尝试登陆三次，
    {"id": 123,"password": "123", "balance": 20000 }
    :return:
    '''
    retry_count = 0
    while username_data['password'] is not True and retry_count < 3:
        username_file = '%s.json' % username
        if os.path.isfile(username_file):
            with open(username_file, 'r', encoding='utf-8') as f:
                username_data = json.load(f)
                print(username_data['password'])
                print(password)
                if username_data['password'] == password:
                    return account_shopping
                else:
                    print("\033[31;1mAccount or Passwordoes not correct!\033[0m")
        retry_count += 1
    else:
        print("Account [%s] try logging too many times..." % username)
        exit()