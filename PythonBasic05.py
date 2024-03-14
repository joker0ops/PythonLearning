message = input("Please input a number: ")
# input函数能够让程序暂停等待用户输入一些文本，并将该文本理解为字符串
# 当获取到用户输入后将字符串赋值给message变量，同时input函数会接收一个参数用于要向用户显示的提示
# while循环
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []
while unconfirmed_users:
    value = unconfirmed_users.pop()
    confirmed_users.append(value)
print(confirmed_users)
# 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)


# 函数
def display_message(title):  # 形参
    print(f"Hello, {title.title()}")


display_message("mike")  # 实参


def describe_pet(animal_type, pet_name):
    print(f"This is {pet_name.title()}, it is a {animal_type}.")


# 位置实参：基于实参的顺序将函数调用中的每个实参都关联到函数定义中的一个形参。
describe_pet("dog", "Jake")
# 关键字实参：在实参中将名称和值直接关联起来，所以向函数传递实参时不会混淆。不需要考虑顺序。
describe_pet(animal_type="dog", pet_name="mike")


# 当使用形参并给形参指定默认值时，若在函数调用时给形参提供实参，则使用实参值，若不指定则使用默认值
def function(def_num=1):
    print(def_num)


function(2)


# 返回字典&让函数形参变成可选的
def build_person(firs_name, last_name, age=None):
    # 这里将age的默认值设置为None(表示变量没有值)使其变成可选的参数，在条件测试中，None相当于False
    """返回字典，其中包含有关一个人的信息"""
    person = {"first_name": firs_name, "last_name": last_name}
    if age:
        person["age"] = age
    return person


He = build_person("Jimi", "hendrix", 17)
print(He)


# 传递列表并在函数中修改列表
def exchange_items(unworked_missions):
    """
    : param unworked_missions: the missions waiting for print
    : param worked_missions: the missions which was printed
    : return: worked_missions
    """
    worked_missions = []
    while unworked_missions:
        item = unworked_missions.pop()
        print(f"Mission {item} has worked.")
        worked_missions.append(item)
    return worked_missions


def show_missions(worked_missions):
    print("This is missions to show:")
    for item in worked_missions:
        print(item)


unworked_missions1 = ["Halo", "insurgency", "CS", "Batman_Arkham_Knight"]  # 定义成unworked_missions1会显示与形参命名重复
worked_missions1 = exchange_items(unworked_missions1)
# worked_missions = exchange_items(unworked_missions[:]) 在实参中使用复制切片的方式防止函数对实际列表进行修改，在这里函数修改的只是复制的列表
# 虽然这种方式可以保留原始列表中的内容，但是这种方式会浪费内存和时间来创建副本，在问题容量较大时不建议使用
show_missions(worked_missions1)


# 传递任意数量的实参
# 可以使用*号来创建能够接收任意数量实参的形参元组，但要区分是使用位置实参还是关键字实参
# 位置实参
def make_pizza(size, *topping):
    # 在函数调用时，size接收传入的第一个实参，然后将其余所有值都存储在元组toppings中
    print(f"Make a pizza of {size}-inch size, and the tops is:")
    for item in topping:
        print(f"-{item}")
    # print(topping)


make_pizza(5, "delicious", "tasty", "salty")


# 关键字实参
def user_profile(first_name, last_name, **user_info):
    """
    形参**user_info的两个星号使得Python创建一个名为user_info的空字典，并存储从实参中传入的所有键值对
    : param first_name: The first name of a man
    : param last_name: The last name of a man
    : param user_info: Other information of a man
    : return: user_info
    """
    user_info["first_name"] = first_name
    user_info["last_name"] = last_name
    user_info["location"] = "England"
    # 函数中的优先级高，函数中修改字典值可使得实参无效
    print(user_info["field"])
    return user_info


user_profile = user_profile("albert", "einstein",
                            location="princeton",
                            field="physics")
"""
函数调用结果会返回一个未排序的名为user_info的字典，多余的实参将以键值对的形式存储在字典中
"""
print(user_profile)

# 模块调用方式
# 调用整个模块并使用模块内任意的函数和变量
# import module_name
# module_name.function_name()
import Module
print(Module.compare(1, 2))
print(Module.c)

# 导入特定的函数
# from module_name import function_name1, function_name2, function_name3...
# function_name1()
from Module import compare
print(compare(3, 4))

# 使用as给函数或模块指定别名
# import module_name as XXX
# from module_name import function_name as XXX
import Module as Md
from Module import compare as cp
print(Md.printc())
print(cp(5, 6))

# 导入模块中所有函数
# from module_name import *
from Module import *
print(compare(7, 8))
print(printc())
