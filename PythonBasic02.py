# 在Python中，使用方括号表示列表，并用逗号分隔其中的元素
Characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(Characters)
# 访问列表元素，列表支持随机访问控制，也可以通过负数索引访问倒数第x个元素，例如：
print(Characters[-1])
# 在列表中添加元素，除了重新定义列表外，还可以通过以下方式：
Characters.append('o')  # 在列表末尾添加新元素
Characters.insert(0, 'firstly')  # 在第一个位置插入firstly，原来的0号位及之后的元素统一向后移动一位
print(Characters)
del Characters[0]  # 删除某个位置的元素
print(Characters)
a = Characters.pop()  # 可以弹出列表尾的元素，列表中原列表尾元素被删除并赋值到e
# 如果想用pop删除某一位序的元素，则在参数中写入元素的位置
b = Characters.pop(0)
# 根据元素值删除元素使用remove方法，参数写入要删除的元素的值
Characters.remove('b')
# 方法sort可以永久性地修改列表元素的排列顺序，初始是从小到大
Characters.sort()
print(Characters)
Characters.sort(reverse=True)  # 颠倒排列顺序
print(Characters)
cars = ["bmw", "audi", "toyota", "subaru"]
# 函数sorted()可以让你能够按照特定的顺序暂时显示列表元素，同时不影响它们在列表中的排列顺序
print(sorted(cars))
print(sorted(cars, reverse=True))
# 反转列表元素
cars.reverse()
# 函数len()可以快速确定列表的长度
print(len(cars))
Marvel = ["IronMan", "AntMan", "CaptainAmerican", "Hulk", "Thor"]
for i in Marvel:
    print(i)
"""
    循环中，python依次从Marvel中取出一个变量，将其与变量i相关联，打印出来
    在下面的循环中，range函数的范围实际上是1到10
"""
for item in range(1, 11):
    print(item)
# 要创建数字列表，可以使用函数list()将range()的结果直接转换为列表
numbers = list(range(1, 11))
print(numbers)
# 使用range()的第三个参数，通过指定步长来生成数，例如：
even_numbers = list(range(1, 11, 2))  # 在这个示例中，函数range从1开始数然后不断+2，直到达到或超过最终值
print(even_numbers)
# 下面的一个示例演示创建一个列表来包含1-10的平方
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(digits))  # 查找数字列表的最小值
print(max(digits))  # 查找数字列表的最大值
print(sum(digits))  # 计算数字列表的和
# 列表解析使得你只需编写一行代码就能生成这样的列表，这种技术将for循环和创建新元素的代码合并成一行并自动附加新元素
squares2 = [value ** 2 for value in range(1, 11)]  # 该行代码以value作为迭代元素（从1到10），每次将迭代元素的平方作为列表元素的值
print(squares2)
"""
    切片操作：可以通过指定使用的第一个元素和最后一个元素的索引，切片操作与range具有相类似的特征，如要
    输出列表的前三个元素，则需要指定索引[0:3]，将返回索引0，1，2
    [x:y]从第x位开始取，取y位
"""
squares3 = [(value*2+1) for value in range(1, 11)]
print(squares3[0:3])
print(squares3[:4])  # 如果没有指定第一个索引，Python将从头开始
print(squares3[3:])  # 如果没有指定第二个索引，Python将提取到最后一个元素
print(squares3[-3:])  # 提取最后三个成员
# 遍历切片
for item in squares3[:3]:
    print(item)
# 复制列表：创建一个包含整个列表的切片
copy_squares3 = squares3[:]
print(copy_squares3)
# python中，不可变的列表称为元组
created = ('a', 'b,', 'c', 'd')
print(created[0])
print(created[1])
# created[2]='d' 该行为会报错
# 遍历元组的元素和列表操作相同
# 如要修改元组中的元素，需要重新定义整个元组
created = ('H', 'e', 'l', 'l', 'o')
# 创建只有一个元素的元组
created2 = ('a', )
