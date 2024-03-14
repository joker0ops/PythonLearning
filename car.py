class Car:
    """模拟汽车的尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # 设定默认值属性
        self.odometer_reading = 0
        self.gas_tank = 56

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印关于汽车里程的信息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """更新关于汽车里程的信息"""
        self.odometer_reading = mileage
        # 添加逻辑，禁止把里程数回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        if miles < 0:
            return
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print(f"Your tank has {self.gas_tank}L gas.")


class Battery:
    """电动车电瓶模拟，可以应用于电动汽车"""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}--kwh battery.")


# 继承
"""
    如要编写的类是另一个类的特殊版本，可以使用继承。当一个类继承另一个类时，将自动获得另一个类的!!!所有属性和方法!!!。原有的类称为父类，而新类称
    为子类，子类继承了父类的所有属性和方法，同时还可以定义自己的属性和方法，在继承时，通常需要调用父类的方法__init__()。这将初始化在父类__init
    __()方法中定义的所有属性，从而让子类包含这些属性。
    创建子类时，父类必须包含在当前文件中，且位于子类前面，定义子类时，必须在圆括号内指定父类的名称。方法__init__()接受创建Car实例所需的信息
"""


class ElectricCar(Car):
    """电动汽车的模拟，继承自汽车模拟"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # super()是一个特殊函数，使得程序员可以调用父类的方法，这行代码让Python调用Car类的方法__init__()，让ElectricCar实例包含父类__in
        # it__()方法中定义的所有属性，父类也称为超类
        self.battery = Battery()  # 所有电动汽车的实例都会包含它，所有汽车实例都不包含它
        """
        这里声明了一个Battery实例，并将该实例赋值给ElectricCar的属性battery
        """

    def fill_gas_tank(self):
        """电动汽车没有油箱，所以重写汽车的该方法，使得有人对电动汽车调用此方法时忽略Car类中的fill_gas_tank，而只是关注子类中的方法"""
        print("This car doesn't need a gas tank!")


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23  # 直接修改属性的值
my_new_car.read_odometer()
my_new_car.update_odometer(12_500)  # 通过方法修改属性的值，传入实参并将其赋值给self.odometer_reading
my_new_car.read_odometer()
my_new_car.increment_odometer(14)  # 通过递增的方式控制用户修改属性值，但能够访问程序的人都可以通过直接访问属性来将里程表修改为任何值
my_new_car.read_odometer()
my_tesla = ElectricCar("tesla", "model s", 2019)  # 创建电车实例
print(my_tesla.get_descriptive_name())  # 使用父类的方法
my_tesla.battery.describe_battery()  # Python先在实例my_tesla中查找属性battery，并对存储在该属性中的Battery实例调用方法describe_battery
