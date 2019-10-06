import  os
import  sys

#添加环境变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from shopping_mall import shopping_main

'''购物车程序的执行文件'''

if __name__ == '__main__':
    shopping_main.run_shopping()