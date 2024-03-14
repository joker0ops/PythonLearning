import json
# 文件操作
"""
    关键字with使得Python在用户不需要访问文件后将其关闭，这比单纯地通过open()和close()函数打开和关闭文件更加稳妥
    如果使用close()关闭文件，那么如果程序出现Bug导致close()函数未能执行，文件将不会关闭
    如果过早地调用close()，可能会使得使用文件时已经关闭，导致更多错误
    但是使用with关键字时，open()返回的文件对象只在with代码块内部可用
"""
with open("LoadingFile.txt") as file_object:  # 函数open()接收一个文件位置+文件名并返回一个表示文件的对象，Python将该对象命名为file_object
    contents = file_object.read()  # 使用read()方法读取文件全部内容(包括空格和制表符)会返回一个长字符串，且到达文件末尾时还会返回一个空字符串
print(contents.rstrip())  # 这个多出来的空字符串会以空行的形式展现，需要使用rstrip()方法消除右空格
"""
    在显示文件路径时，Windows系统使用反斜杠'\\'，而Linux系统使用斜杠/
    Windows系统示例：C:\\path\\to\\file.txt
    Linux系统示例：/home/joker/code/python.txt
    在open函数中使用绝对路径和相对路径都可以
"""
with open(".\\LoadingFile.txt") as Pi_Object:
    # 对文件实行逐行读取
    for item in Pi_Object:
        print(item.rstrip())  # 这种操作会使得每行末尾都有两个换行符，一个来自文件本身，一个来自print()函数，这些换行符都可以用strip类方法消除
    # 创建一个包含文件各行内容的列表
    lines = Pi_Object.readlines()  # readlines()方法读取文件中的每一行，并将其存储到一个列表中，最后赋值给lines
    pi_string = ""
    # 将各行加入pi_string变量
    for line in lines:
        # 使用strip方法去除所有空格
        pi_string += line.strip()
    # 最后根据需要也可以使用int()或float()对字符串进行转换
    print(pi_string)
    print(len(pi_string))

# 大文件处理
filename = "pi_million_digits.txt"
with open(filename) as file_object2:
    contents = file_object2.readlines()

PI = ""
for line in contents:
    PI += line.strip()

print(f"{PI[:50]}...")
print(len(PI))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in PI:  # 注：空串是任何字符串的子串
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday doesn't appears in the first million digits of pi!")

# replace方法的使用：
message = "I really like dogs."
message.replace("dog", "cat")  # 替换字符串中所有的dog子串
print(message)

# 写入文件
filename = "programming.txt"
with open(filename, 'w') as file_object3:
    # 以写入模式打开文件，当文件不存在时，函数open()将自动创建文件
    # 用写入模式打开文件时要小心，因为若指定的文件已经存在，Python将在返回文件对象前清空文件内容
    file_object3.write("I love programming.\nI love creating new games.\n")
    # 函数write()不会在写入的文本末尾自动添加换行符，需要自行添加，否则两句会独占一行
    """
    文件打开模式：
    'w'：写入模式
    'r'：只读模式
    'a'：附加模式
    'r+'：读写模式
    如果省略了模式实参，Python将会以默认的只读模式打开文件
    注意：Python只能将字符串写入文本文件。如要存储数值数据，需要先用str()将其转换为字符串格式
    """
with open(filename, 'a') as file_object4:
    # 以附加模式打开文件，当文件不存在时，函数open()将自动创建文件
    # 以附加模式打开文件时，Python不会在返回文件对象前清空文件内容，而是将写入文件的行添加到文件末尾
    file_object4.write("I also love finding meaning in large datasets.\n")
    file_object4.write("I love creating apps that can run in a browser.\n")
# Python每产生一个错误都会创建一个异常对象，异常是通过try-except代码块处理的，使用该代码块时即使出现错误也不会traceback而是继续运行
a = input("Please input a number as Division: ")
b = input("please input a number as b: ")
try:
    print(int(a) / int(b))
except ZeroDivisionError:
    print("You can't divide by zero ")
"""
    另一种结构：
    try:
        尝试
    except 异常对象:
        异常处理
    else:
        如果未发现异常将会执行的程序
"""


def count_words(filename):
    """计算一个文件大致包含多少单词"""
    try:
        with open(filename, encoding="utf-8") as f:
            # 若系统默认编码和文件编码不一致，则必须使用encoding参数
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} doesn't exist.")
        # pass
        # 该处也可以换成pass，代表静默异常——即什么都不做
    else:
        words = contents.split()
        # 使用方法split来根据一个字符串创建一个单词列表
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


for item in range(1, 11):
    filename = input("Please input a filename: ")
    count_words(filename)

# JSON模块：用于对文件存储或加载数据，还可以使用JSON在Python程序之间分享数据
numbers = [2, 4, 6, 7, 9, 10]
# 若numbers列表使用range生成，需要使用list()转义：numbers = list(range(1, 11))
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
with open(filename, 'r') as f:
    numbers2 = json.load(f)
print(numbers2)


# JSON应用实例
def get_stored_username():
    """如果已经存储了用户名，就获取它"""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("Please input your name: ")
    filename = "username.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We will remember you when you come back, {username}.")
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()


greet_user()
