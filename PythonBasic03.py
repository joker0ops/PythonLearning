# if语句的使用
print(1 == 1)  # 首先要了解比较运算符的返回值，如果是True就会被if处理，False则会被if忽略
print('abc' == 'ab')
str1 = "Hello"
str2 = "hello"
if str1 != str2:  # 逻辑表达式中可以直接判断两个字符串是否相等
    print("The string is not same")
num1 = 1
num2 = 1
if num1 == num2 and str1 == str2:
    print("yes")
elif num1 == num2 or str1 == str2:
    print("right")
else:
    print("no")
# 对列表中的值进行查询判断
# 检查特定值是否包含在列表中：
cars = ["bmw", "Audi", "Bench", "Toyota"]
if "bmw" in cars:
    print(True)
# 检查特定值是否不包含在列表中：
elif "Audi" not in cars:
    print(False)
else:
    print(True)
# 确定列表不是空的，在if语句中将列表名作为条件表达式时，Python将在列表中至少包含一个元素时返回True，并在列表为空时返回False
trip = []
if trip:
    print(True)
else:
    print(False)
