# Python中的字典元素以键值对的形式存储，类似于C中的结构体，每一个键都与一个值相关联，与键相关联的值可以是
# 字典使用的第一种类型：存储同一类对象的不同信息
alien = {
    "color": "green",
    "points": 5
}
# 访问字典中的值
print(alien['color'])
# 字典是一种动态结构，可以随时添加键值对，直接使用赋值的方式指定字典名，键名和值即可
alien["method"] = "post"
print(alien)  # 字典直接打印
# 在使用字典来存储用户提供的数据或在编写能自动生成大量键值对的代码时，通常需要先定义一个空字典
alien_0 = {}
# 若是修改字典的值，直接按照赋值的方式修改即可
# 对于不再使用的信息，可以使用del语句，指定字典名和要删除的键来删除
del alien["method"]
print(alien)
# 对于字典的另一种使用方式，即存储不同对象的同一类信息
favorite_languages = {
    "jen": "Python",
    "sarah": 'C',
    "edward": "ruby",
    "phil": "Python"
}
# 使用随机存取方式访问字典元素时，若指定的键不存在会报错，可以使用get方法指定任意键，当该键不存在时返回一个指定的默认值（可选）
# 若没有指定可选的测试值时，get将返回None
point_language = favorite_languages.get("Jack", "No such key")
# 使用for循环迭代器的方式遍历字典
for key, value in favorite_languages.items():
    # 方法items()返回一个键值对列表，for循环将依次将两个列表中的元素分别赋值给key和value两个变量
    print(f"\nkey: {key}")
    print(f"value: {value}")
# 遍历字典中的所有键而不遍历值
for key in favorite_languages.keys():
    print(key)
    # 也可以使用当前key变量来访问键key所对应的value
    print(favorite_languages[key])
# keys()方法与items方法类似，但只是返回一个键的列表
if "sarah" in favorite_languages.keys():
    print("search successfully!")
# 可以在for循环遍历之前对字典使用sorted函数进行临时排序
# 如果只想获取字典中的所有值，可以使用values()方法返回一个值的列表
for value in favorite_languages.values():
    print(value)
print("\n")
# 可以发现，这种方法获取值是不会剔除掉重复项的，可以使用集合set函数，使得列表中的元素独一无二
for value in set(favorite_languages.values()):
    print(value)
# 对于普通集合可以使用花括号来定义，其与字典的区别是集合是单一元素，而字典是键值对，而且集合不会以特定的顺序存储元素
set1 = {'1', '2', '3', '4', '5', '6', '1'}
print(set1)
