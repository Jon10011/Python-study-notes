# coding=utf-8
#Time模块
""
"1.time"
import time
t1 = time.time()
for i in range(10000000):
    pass
t2 = time.time()
print t1,t2

"2,。ctime(...)将一个时间戳（默认为当前时间）转换成一个时间字符串"
print '----------------------------'
print time.ctime(t1)

"3.asctime()将一个struct_time(默认当前时间，转换成字符串)"
print '----------------------------'
print time.asctime()

"4.clock(）第一次调用，返回的是程序运行实际时间" \
"第二次调用，返回第一次调用后的间隔时间"
print '----------------------------'
print time.clock()
print time.clock()

"5.sleep()休眠指定的时间"
print '----------------------------'
time.sleep(2)
print time.time()

"6.gmtime()将一个时间戳(默认当前时间)转化为一个0时区的struct_time(结构化时间)"
print '----------------------------'
print time.gmtime()
print time.gmtime(time.time())
print time.gmtime(888888888)
"7.localtime()将一个时间戳转化为当前时区的结构化时间（struct_time）"
print '----------------------------'
print '生成struct_time1:',time.localtime()
print '生成struct_time2:',time.localtime(88888888)

"8."