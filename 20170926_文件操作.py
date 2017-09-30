# coding=utf-8
""
"1.open()函数文件打开操作"
"语法：open(name[,mode[,buffering]])"

with open('test.txt') as f:
    #content = f.read()
    print f.tell()

    print f.readlines()
    #print content
print '-------------------------------------------'
with open(r'F:\Python\Month09\test01.txt','r')as f:
    #print f.write('this is a text')
    print f.read()
"'w'以写的方式打开文件，覆盖文件的所有内容，如果没有这个文件，创建文件"
"'w+'读写，创建新文件，读写指针在末尾，如果文件存在会覆盖之前的内容"

"'r'读,文件存在直接读，文件不存在报错" \
"'r+'读写，不创建新文件，文件读写指针在开头"

"'a'追加 文件不存在聚创建文件，文件存在就添加到文件内容，只写不读" \
"'a+'读写，创建新文件，读写指针在末尾，不会覆盖这个文件之前的内容"
#f.flush() 将内存里的东西存到硬盘

#f.seek(0,0) 读取缓存指针位置
"seek()修改访问文件中指针的位置 File_object.seek(offset,whence)"
"offset 开始的偏移数，也代表需要移动偏移的字节数"
"whence:" \
"0表示从头开始计算" \
"1表示以当前位置为原点进行计算" \
"2表示以文件末尾为原点进行计算"

print '------------------------------------------------'
with open ('test04.txt','a') as f:
    print f.tell()#初始位置
    f.write('*****I  LOVE Python\n')
    f.write('*****I  LOVE Python\n')
    print f.tell()#当前位置
    f.flush()
    f.seek(-10,2)
    print 'now:',f.tell()
    #print f.read()
    print '-----------------------------------------------'
import mysql.db