#coding=utf-8
import time,thread,threading
#使用类的重写方法启动线程
class Mythread(threading.Thread):

    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print 'hello：%s'%self.name

if __name__ == '__main__':
    t1 = Mythread('Jon')#类的实例化
    t2 = Mythread('James')
    t1.start() #start启动线程
    t2.start()
print '\n-------------------------------------------------------------'
#Threading 直接调用start启动线程
def say(name):
    print 'function say start time:',time.ctime()
    print 'hello:%s'%name
    time.sleep(3)
    print 'function say finished time:',time.ctime()

def hi(name):
    print 'function hi start time:',time.ctime()
    print 'hello:%s'%name
    time.sleep(2)
    print 'function hi finished time:',time.ctime()

def main():
    print 'hello,main'
if __name__ == '__main__':
    #target是线程调用的函数对象，args是函数需要的参数
    t3 = threading.Thread(target=say,args=('aaa',))
    t4 = threading.Thread(target=hi, args=('bbb',))
    t5 = threading.Thread(target=main)
    t3.setName('say')#设置线程名
    t3.start()
    print t3.getName()#打印线程名
    t4.setName('hi')
    t4.start()
    print t4.getName()
    t5.setName('main')
    t5.start()
    t3.join()
    t4.join()
    t5.join()
    print t5.getName()