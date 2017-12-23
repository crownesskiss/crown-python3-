#usr/bin/python3
#coding:utf-8
#coding= gpk2312
'''
字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
'''
d = {'zhangbo':0012,'zhanggege':0013}
'''
键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

一个简单的字典实例：
d = {key1:value1,key2:value2}
'''
dict = {'Alice':1234,'zhangbo':1235}
print(dict)
#for temp in dict:
    #也可创建
dict1 = {'abc':456}
dict2 = {'123':123, 98.6:37}
print("访问字典中的值")
print(dict2['123'])
print(dict2[98.6])
print("向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:")
dict5 ={'Name':'Runoob','Age':7,'class':'First'}
print("更新字典中的信息")
dict5['Age'] = 29
dict5['School'] = '岸边中学'
del dict5['Name']
print(dict5)
dict5.clear()
type(dict5)
dict6 = {'name': 'zhangbo','Age':56,'Name':'小菜鸟'}
print("dict['Name']:",dict6['name'])
print(len(dict6))
print("字典内置函数")
String =str(dict6)
print(String)
dict6.values()
dict6.items()
