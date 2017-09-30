# coding = utf-8
import os
def getdir(dirpath,level=0):
    level +=2
    for name in os.listdir(dirpath):
        print ('--'*level+'|'+name)
        if os.path.isdir(dirpath+'\\'+name):
            getdir(dirpath+'\\'+name,level)
dirpath = raw_input('please input your dirpath:')
getdir(dirpath,1)