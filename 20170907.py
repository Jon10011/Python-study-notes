# -*- coding: utf-8 -*-
#Expandtabs

"""
a = '123   123'
a.expandtabs()
print (a.expandtabs().count(' '))
print (a.count(' '))
print (a.isalnum())
b = 'abc123'
print (b.isalnum())
#判断全字母
print (b.isalpha())
c = 'abcdwfd'
print (c.isalpha())
d = 'abcd dfds'
print (d.isalpha())
e = '12121132'
#判断全数字
print (e.isdigit())
print (a.isdigit())
f = ' abcd   '
#去除前后空格
print (f.lstrip())
print (f.rstrip())
#查询方法
print (dir(str))
print (help(str.strip))
#列表--有序的集合，可随时添加删除元素。写在[]之间用‘，’分开
g = [1,2,3,4]
print (type(g))
print (g[1])
h = [1,2,3,[a,b,c],(1,2)]
print (h[3][1])

a1 = [1,2,3,4,1,5]
a1.pop(4)
print (a1)
a1.remove(4)
print(a1)
#count 统计列表某元素出现的次数
#reverse 将列表元素反向排列
a2 = [4,3,2,1]
a2.reverse()
print (a2)
#sort 对列表进行排序
a2.sort()
print (a2)

#列表切片操作 适用于:字符串，列表，元组 .[start:stop:step]
"左闭右开，省略，负数索引，步长，浅拷贝"
b1 = [1,2,4,5,7,0,6]
print(b1[2])
print(b1[1:3])
b2 = range(1,101)
print (b2)
print(b2[0:10]) #"左闭右开"
print(b2[:10])#省略
print(b2[-11:])#负数索引
print(b2[0:100:10])#步长10 切片
print(b2[::10])
#1到100之间取3的倍数
print(b2[2:100:3])
#不大于50的 5的倍数
print (b2[4:50:5])
"倒序切片"#负数索引
print(b2[-4:-1:2])#[97,99]
print(b2[-10:])
print(b2[41:100:6])
print (b2[5::6][-10:])#取出全部6的倍数，倒序取出后十位
print (b2[-59::6])
"""

"set(集合)"#互异性，无序性（因此集合无法用于索引）
"特点：无序不重复性，基本功能是进行成员关系测试和删除重复元素"
c2=[1,2,3,4,4,3,2,1,5,6,9]
S = set(c2)
print(S)
"创建空的字典"
S={}
print(type(S))
"创建空的集合"
S = set()
print(type(S))
"集合添加元素"
S1 = set([1,2,3,4,5])
S1.add(6)
print(S1)
S1.update({6,7,8,9})
print(S1)
"创建不可变集合（无法使用add等方法）"
L = [1,2,3]
S2 = frozenset(L)
print (S2)
S3 = {1,2,3,4,5,6,7,8,9}
print(S3.pop())
print(S3.pop())
print(S3.pop())
print(S3.pop())
print(S3.pop())
print(S3.pop())
print(S3)