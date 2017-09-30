#_*_ coding:utf-8_*_
#浅拷贝
L=range(1,11)
L1 = L #传引用
L2 = L[:] #浅拷贝
print (L1)
print(L2)
L[3] = 'range'
"""
print(L)
print(L1)
print(id(L))
print(id(L1))
print (L2)
"""
"负数步长：索引不会变，正数步长默认从左向右取值（start<stop），负数步长默认从右往左取（start>stop）"
print(L[5::-2])#负数步长切片。默认索引从右到左


#Tuple(元组)
"元组是不可变的Python对象序列，类似列表，使用小括号，',隔开'"
T = (1,2)
print(type(T))
"T[1] = 4"
"print(T)"#元组内容不可变
T1 = (1,)#创建单个元素的元组需要加“，”
print(type(T1))
print(dir(tuple))
T2 = (1,2,3,4,5,2)
print(T2.count(2))
print(T2.index(2))
print(T2.index(2,2))
print(T2.index(2,1))
print(T2.index(2,-4))

#Python 运算符汇总
"算数运算符"
"比较（关系）运算符"# ==，！=(<>)，>,<,>=,<=
"赋值运算符"# =，+= ，-=，*= ，/=，%= ，**= ，//=
"逻辑运算符"
# And--与，
a = 10
b = 20
print(a and b)
c = 0
print(c and b)
# Or--或
#Not--非

"位运算符"
#二进制运算符
"&--按位与运算符：参与运算的两个值，如果两个相应位都为1，则该位的结果为1，否则为O"
"|--按位或运算符：只要对应的两个二进位有1就是1，同为0才为0"
"^--按位异或运算符，相异为1，否则为0 "
"~--按位取反运算符，0->1,1->0"
">>""<<"

"成员运算符"# in ， not in
"身份运算符"#is , is not