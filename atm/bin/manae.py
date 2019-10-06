import  os
import  sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #找到路径
sys.path.append(BASE_DIR)          #添加路径

from core import  main
'''管理程序的执行文件'''
if __name__ == "__main__":
    main.run_manage()
