#coding=utf-8
""
"数据库"
import MySQLdb
#打开数据库连接
db = MySQLdb.connect('localhost','root','123456','test')
#使用cursor()方法获取操作游标
cursor = db.cursor()
sql = "UPDATE USER SET PASSWORD = '123456' WHERE NAME='%s'"%('jon')
cursor.execute("select version()")
data = cursor.fetchone()
print "Databases version:%s"%data
try:
    #执行sql语句
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    #发生错误回滚到操作以前的状态
    db.rollback()
db.close()