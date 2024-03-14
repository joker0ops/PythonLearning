# 该程序中的各个方法并不会像函数一样对字符串产生实质性的变化
message = "hello"
print(message)
message = "Hello World"
print(message)
# Python是解释型语言，会逐行解释执行，因此对于变量python只记录变量的最新值
# 由于Python不检查变量名与上文的匹配，因此在变量命名中尽量不要用小写l和大写O，容易看错
# 字符串用双引号还是单引号都可以
print("The language 'python' is named after Monty Python, not the snake.")
name = "ada lovelace"
print(name.title())  # 首字母大写
print(name.upper())  # 全大写
print(name.lower())  # 全小写
print(name)
# 在字符串中插入变量的值，可以在前引号前加上字母f，再将要插入的变量放在花括号内
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello! {full_name.title()}!")
name2 = name.rstrip()  # 去右空白
name3 = name.lstrip()  # 去左空白
name4 = name.strip()  # 去空白
print(name)
num1 = 3**3
num2 = 3**2
print(f"{num1} {num2}")
# python用**表示乘方运算，任意两个数相除时，结果总是浮点数
# 当定义很大的数的时候，可以使用下划线将数字分组，python不会打印这些下划线，如
num4 = 123_000_000_000
# python同时给多个变量赋值
x, y, z = 0, 0, 0
# python中没有常量，通常用全大写字母表示常量
