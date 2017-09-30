#coding=utf-8
import time,thread,threading
def say(name):
    print 'function say start time:',time.ctime()
    print 'hello:%s'%name
    time.sleep(3)
    print 'function say finished time:',time.ctime()

def hi(name):
    print 'function say start time:',time.ctime()
    print 'hello:%s'%name
    time.sleep(2)
    print 'function say finished time:',time.ctime()

def main():
    say('Jon')
    hi('James')

if __name__ == "__main__":
    main()