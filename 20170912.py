#coding:utf-8
#python 模块的导入以及包的制作
#模块
"使用import语句将一个源代码文件作为模块导入"
"导入方式："
"1.直接导入（可同时导入几个模块）;"
"2.用import...as...(别名，使用别名后无法使用原名)"
"3.使用from语句将模块中的对象直接导入到当前名字空间,支持“，”分割导入多个对象"
"4.as也可以和from搭配使用"
"5.自定义模块"
"注意"
if __name__ == '_main_':
    # 作为脚本运行
    print 'this is main func'
else:
    # 作为模块导入运行
    print 'this is module'

#包（package）
"包是一个有层次的文件目录结构，它定义了一个有模块和子包组成的Python应用程序执行环境"
"作用：" \
"为平坦的名称空间加入有层次的组织结构"
"允许程序员把有联系的模块组合到一起"
"允许分发者使用目录结构而不是一大堆混乱的文件"
"帮助解决有冲突的模块的定义"

#作用域
"LEG--LEGB"
"""
L：local,局部作用域，即函数中定义的变量
E:enclosing，嵌套的父级函数的局部作用域
G:global，全局变量，即模块级别定义的变量
B:bulit-in，系统中定义的变量，比如int，byte...
"""

x = int(1.5)#int bulit-in
G = 0 #global
def func():
    E = 1 #enclosing
    def func1():
        L = 2 #local
"搜索变量优先级顺序依次是：局部作用域>外层作用域>当前模块找那个的全局>Python内置作用域"

#闭包
"python 中的闭包从表现形式上定义为：如果在一个内部函数里，" \
"对外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认定为闭包（closure）"
def outer(a):
    def inner(b):
        return b + a
    return inner #此处inner是一个闭包
p = outer(23)
q = outer(89)
print p(100)
print '---------------------'
print q(98)
print '---------------------'

def func():
    abc = []
    for i in range(3):#[0,1,2]
        def func1():
            return i*i
        abc.append(func1)
        print abc[0]()
    print abc[0](),id(abc[0]),abc[1](),id(abc[1]),abc[2](),id(abc[2])
    return abc #abc[func1,func1,func1]
f1,f2,f3 = func()#func1
print 'f1:',f1(),id(f1)#0*0->循环到2*2
print 'f2:',f2(),id(f2)#1*1->循环到2*2
print 'f3:',f3(),id(f3)#2*2
print '---------------------'





