"""
Python是一个模块化语言，函数以及其他的一些预处理可以存储在模块文件中，再将模块导入到主程序中等待调用
模块是扩展名为.py的文件，包含要导入到程序中的代码
"""


def compare(a, b):
    if a > b:
        return a
    else:
        return b


c = 4


def printc():
    print(c)
