# -*- coding: utf-8 -*-
#递归:函数调用自己
"避免无限循环"
"例子：求阶乘"
"""
def F(n):
    if n == 0 or n == 1:
        return 1
    return F(n-1)*n
print F(3)
print F(6)
"""
#汉诺塔
"""
def func(n,A,B,C):
    if n==1:
        print "%s-->%s"%(A,C)
    else:
        func(n-1,A,C,B)
        func(1,A,B,C)
        func(n-1,B,A,C)
func(64,'A','B','C')
"""
#异常处理
"""
try:
    <语句>#运行别的代码
    except<名字>：
    <语句>#如果try部分引发了name异常
    except<名字>，<数据>：
    <语句> #如果引发里‘name’异常，获得附加的数据
"""
print "input a number,and i'll devide them"
print "input 'q' to quit"
while 1:
    fir = raw_input('\nfirst number:')
    if fir == 'q':
        break
    sec = raw_input('\nsecond number:')
    try:
        ans = int(fir)/int(sec)
    except ZeroDivisionError:
        print 'you sec is wrong(0)'
    else:
        print ans

"""
try:
#要执行的语句
finally：
#退出try会执行这个代码
"""
"""
使用raise触发异常 
"""
def errfunc(n):
    if n<1:
        raise Exception('Invalid n!',n)
try:
    errfunc(0)
except Exception:
    print 'the erroe is raise'
else :
    print 'no error'