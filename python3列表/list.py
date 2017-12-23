#usr/bin/python3
#coding:utf-8
#coding= gpk2312
#序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。

#Python有6个序列的内置类型，但最常见的是列表和元组。

#序列都可以进行的操作包括索引，切片，加，乘，检查成员。

#此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。

#列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。

#列表的数据项不需要具有相同的类型

#创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
list1 = ['Google','Runoob',1997,2000]
print(list1)
list2 = [1,2,3,4,5]
print(list2)
#访问列表中的元素

list3 = ['你好','世界','hello',2017,1998]
print("访问列表中的元素:",list3[3])
print("-----------------------------")
print("访问列表中的元素:",list3[0:4])
print("for 循环输出列表中的元素")
for temp in list3:
    print(temp)
print("更新列表之前")
for temp in list2:
    print(temp)
print("更新列表中的元素")
list2[2] = 'zhongbo'
for temp in list2:
    print(temp)
#删除列表中的元素
print("删除之前的列表")
for temp in list3:
    print(temp)
print("删除列表之前")
del list3[2]
print("删除列表元素之后的列表")
for temp in list3:
    print(temp)
#python列表脚本操作符
print("列表的长度:",len(list2))
print("列表连接")
list4 = list1 +list2
print(list4)
print("重复列表元素")
print(list2*3)
print("查看元素时候在列表中")
print(4 in list2)
print("截取列表")
L = ['google','windows','dell','mac','lenovo']
print(L[2])
print("反向截取")
print(L[-2])
print(":冒号输出截取位置之后的所有元素")
print(L[-2:])
print("列表且套")
a = ['a','b','c','d']
n = [1,2,3,4,5,6,7]
x = [a,n]
print(x)
print('列表中的最大元素')
print(max(x))
print("在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）")
x.extend(L)
print(x)
print("统计某个元素在列表中出现的次数")
num = x.count(1)
print(num)
x.append("zhangbo nishige haoren ")
print(x)
print("方向列表中的元素")
x.reverse()
print(x)
print("从列表中找出某个值第一个匹配项的索引位置")
#x.index(2)
lis = [23,1,4,0,34,11,2323,90]
lis.sort()
print(lis)
print("清空列表")
#lis.clear()
print("列表辅助")
lis.copy()
print(lis)
