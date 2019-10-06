import  os
import sys

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   #从系统模块中获取项目跟目录
sys.path.append(base_dir)     #把根目录添加到解释器模块

from core import main    #引入解释器的寻找目录之后再引入其他模块中的文件
#print(base_dir)

if __name__=='__main__':
    main.run_atm()


