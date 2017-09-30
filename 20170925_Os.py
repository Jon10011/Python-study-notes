# coding=utf-8
#os模块
""
"1.os.sep 可以取代操作系统特定的路径分隔符 '\'"
import os
print os.sep
"2.os.name 字符串指示你正在使用的平台 'windows-->nt'"
print os.name

"3.os.getenv()读取环境变量"
print os.getenv('path')

"4.os.listdir()返回指定目录下的所有文件和目录名，但是没有列出来什么事目录什么是文件"
print os.listdir('F:\Python\Month09')

"5.os.remove()用来删除一个文件"
"6.os.rmdir('dir_name')删除指定目录"
"7.os.mkdir('dir_name')创建目录"
print os.mkdir('F:\Python\Month09\Month10')
print os.rmdir('F:\Python\Month09\Month10')

"8.os.makedirs('a/b/c'）递归创建目录"
"9.os.getewd()得到当前工作目录，即当前Python脚本工作的目录路径"
"10.os.chdir('file_path')改变工作目录"

"11.os.walk('file_path'),可以起到一个遍历目录的效果"
for i in os.walk('F:\Python\Month09'):
    print i
"""
返回三个返回值：（dirpath,dirnames,filenames）
Dirpath:目录路径
Dirnames:要查找的目录下的所有目录名
Filenames:所有文件名
"""

"12.os.system()用来运行shell命令"
print os.system('dir')

#os.path 模块
"1.os.path.split()返回一个路径的目录名和文件名"
print os.path.split('F:\Python\Month09\day0907.py')

"2.os.path.splitext():分离文件名和扩展名"
print os.path.splitext('F:\Python\Month09\day0907.py')

"3.os.path.isfile()和os.path.isdir(),分别检验给出的路径是一个文件还是目录"
print os.path.isfile('F:\Python\Month09\\20170907.py')
print os.path.isdir('F:\Python\Month09\\20170907.py')

"4.os.path.getsize(name)返回文件大小"
print os.path.getsize('F:\Python\Month09\\20170907.py')

"5.os.path.abspath()获得绝对路径"
"6.os.path.join(path，name)链接目录与文件名或目录"
print os.path.join('F:\Python\Month09','20170907.py')

"7.os.path.basename(path)返回文件名"
print os.path.basename('F:\Python\Month09\\20170907.py')

"8.os.path.dirname(path)返回文件路径"
print os.path.dirname('F:\Python\Month09\\20170907.py')

#递归查找目录

def getdir(dirpath,level=0):
    level +=2
    for name in os.listdir(dirpath):
        print ('--'*level+'|'+name)
        if os.path.isdir(dirpath+'\\'+name):
            getdir(dirpath+'\\'+name,level)
dirpath = raw_input('please input your dirpath:')
getdir(dirpath,1)