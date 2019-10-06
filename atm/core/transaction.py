import  json
from conf import  settings
from core import  accounts

def make_transaction(log_obj, account_data, tran_type, amount, **others):
    '''
    处理所有的用户的交易
    :param log_obj:
    :param account_data: user account data
    :param tran_type:   transaction type
    :param amunt:     transaction amount
    :param others:    mainly for logging usage
    :return:
    '''
# 将字符串类型转换为float类型
    amount = float(amount)
    #tran_type 交易类型
    if tran_type in settings.TRANSACTION_TYPE:
        # 利息金额
        interest = amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        old_blance = account_data['balance']
        if tran_type in settings.TRANSACTION_TYPE:
        # 利息金额
            interest = amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        # 用户原金额
            old_blance = account_data['balance']
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = float(old_blance) + amount + float(interest)
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_blance = float(old_blance) - amount - float(interest)
            # 做一个判断小于0的操作，减钱时对帐户金额进行检查，防止超额
            if new_blance < 0:
                print('\033[31;1mYour credit [%s] is not enough for this transaction'
                          '[%s]'%(account_data['credit'],(amount + interest), old_blance))
                return
            account_data['blance'] = new_blance
        # 保存新的余额返回到文件中
        print('123444')
        accounts.dump_account(account_data)
        log_obj.info("account:%s   action:%s  amount:%s  interest:%s "
                     %(account_data['id'],tran_type,amount,interest))
        return account_data
    else:
        print("\033[31;1mTransaction type [%s] is not exist\033[0m" % tran_type)


