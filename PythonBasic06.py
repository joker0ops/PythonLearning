from random import randint, choice  # 常见Python标准库，随机数标准库，但创建安全相关的项目时不要使用random


# 类，定义中使用首字母大写的单词表示类，类定义时名称后没有圆括号表示没有继承等操作，是从空白创建一个类
class Dog:
    def __init__(self, name, age):
        """初始化属性name和age
           这里的__init__()是一个类默认方法<类中的函数>，每当根据Dog类创建新实例<对象>时，Python都会自动运行它。
           在这个方法的定义中，形参self必不可少，而且必须位于其他形参的前面，每次创建此类的实例时，该方法都会自动运行此
           方法并传入实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
           每当根据Dog类创建实例时，都只需要给最后两个形参name和age提供值
           以self为前缀的变量可供类中的所有方法使用，可以通过类的任何实例来访问，称为属性self.XXX
        """
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到指令时蹲下"""
        print(f"{self.name} sat down!")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")


my_dog = Dog("Willie", 6)
# 创建实例时调用__init__()
print(f"My Dog's name is {my_dog.name}")
print(f"My Dog's age is {my_dog.age}")
# Python先找到实例my_dog，再查找与该实例相关联的属性name
# 在Dog类中引用这个属性时，使用的是self.name
my_dog.sit()
my_dog.roll_over()
# 导入类：
# from car import Car, ElectricCar 从一个模块中导入多个类，但这种方法容易与当前文件中的名称发生冲突，需要注意头部导入的模块
# import car 这种方法导入整个模块，再使用句点表示法访问需要的类，用到模块中的类时均需要包含模块名，因此不会发生冲突
# from module_name import * 不推荐使用这种方式
# 有时候，需要将类分散到多个模块中，以免模块太大或在同一个模块中存储不相关的类，也可以在引入模块后用as对模块命名以区别
# Python标准库
print(randint(1, 10))  # 随机返回一个位于1~10之间包含的整数
arrays = ['a', 'c', 'e', 'd', 'g', 'z']
print(choice(arrays))  # 以列表或元组作为参数，随机返回其中一个元素
# 驼峰命名法
"""
1. 类名中的每个单词首字母都大写，并且单词之间不使用下划线。实例名和模块名都使用小写并在单词之间加上下划线
2. 对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式规定
每个模块也都应该包含一个文档字符串，并对其中的类的用途进行描述
"""
