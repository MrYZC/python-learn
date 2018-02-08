# sys模块

import sys
import os
import math
print(sys.argv) # 文本路径
print(sys.path) #包含当前python解释器能找到的路径
print(sys.platform)
print(sys.version) # 查看python版本
print(sys.exit) # 退出解释器，程序到了sys.exit()就会终止

# os模块
print(os.name) # 返回操作系统类型posix代表linux,'nt'代表windows
print(os.extsep) # 返回.
print(os.environ) # 以系统形式返回系统变量
print(os.devnull) # 返回/dev/null标识符
print(os.linesep) # 返回一个换行符"\n"
print(os.sep) # 返回一个路径分隔符正斜杠""/"
# print(os.listdir(path)) 列表形式列出目录
# print(os.getcwd()) 获取当前路径
# print(os.chdir(path)) 改变当前工作目录到指定目录
# print(os.mkdir(path [,mode = 0777])) 创建目录
# os.makedirs(path, [, mode =0777]) 递归创建目录
# os.remove(path) 移除文件
# os.rename(old, new) 重命名文件或目录
# os.stat(path) 获取文件或目录属性
# os.chown(path,uid,gid) 改变文件或目录所有者
# os.chmod(path,mode) 改变文件访问权限
# os.symlink(src, dst) 创建软链接
# os.path.basename(path) 返回最后一个文件或目录名

# math模块
print(math.pi)
print(math.ceil(5.2))  # 上限 6
print(math.floor(5.2)) #下限 5
print(math.trunc(5.2)) #将数字截尾取整
print(math.fabs(-5.2)) # 绝对值
print(math.fmod(5, 2)) # 返回x%y取余
print(math.factorial(5)) #返回阶乘
print(math.pow(2,3))
print(math.sqrt(5))

