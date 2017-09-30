#coding=utf-8
"python函数"
'''
a = range(100)
print (a)
'''
"形参（形式参数），实参（实际参数）"
"必备参数：实参与形参对应，顺序不可改变（正确的顺序）数量必须和声明时一样"
"命名参数（你的形参在定义的时候没有语法错误）"
def fun(name,age):
    print 'your name is :',name
    print 'your age is :',age
fun(3,'int')
fun(age=3,name='int')
"缺省参数（如range(stop),range(start,stop),range(start,stop,step)）"
"注意：默认参数需要在形式参数表中的位置，即默认参数必须放在标准参数之后定义，如下：name要放在age后面"
def func(age,name = 'for'):
    print 'the name is:',name
    print 'the age is:',age
func(4)
"不定长参数，你可能需要一个函数能处理比当初声明时更多的参数，叫不定长参数，声明时不会具体定义"
"1：一个星号，默认把传递进来的多个参数处理成元组类型"
def func1(*arg):
    print arg
    print type(arg)
    print list(arg)
func1(1,2,3,4,5,6,7,'int','for')
"2：两个星号，参数以键值对的形式传递，默认把传递进来的多个键值对处理成字典"
def func2(**arg):
    print arg
    print type(arg)
    print list(arg)
"错误：func2('int1'=3,'for1'=7,'if1'=12)"
func2(int1=3,for1=7,if1=12)

#函数的高级用法
"匿名函数：（lambda表达式）"
"lambda 参数1，参数2，参数3，参数N：表达式"
goods_list = [('iphone',5800,8922),('ipad',3600,150236),('apple',152222,59541)]
L = sorted(goods_list,key=lambda goods:goods[1])
print L
print goods_list

myfunc = lambda x,y:x+y
print myfunc(1,2)
"sort(),sorted()"

"函数嵌套：外部无法调用"
def func2():
    global func3# 声明为全局函数，外部可调用
    def func3():
        print 'this is inner function,func2'
    return func3()
func2()
"func3():内部嵌套函数，无法打印出来，只能在func2()内部使用"
func3()

"传值：传递一个不可变的数据对象，在函数内部修改不会影响外部的数据"
"传引用：传引用就是实参传递了可变数据对象，这样我们在函数内部可以直接修改原址的值"

a = [1,2,3]
def func4(obj):
    obj = ['a','b','c']
    print id(obj)
    print '内部参数：',obj
func4(a)
print id(a)
print '外部变量：',a

b = [1,2]
def func4(obj1):
    obj1 += ['a','b']#内存地址改变
    print id(obj1)
    print '内部参数：',obj1
func4(b)
print id(b)
print '外部变量：',b