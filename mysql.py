'''
mysql.py 数据库示例
pymysql 操作数据库基本流程
'''

import pymysql

#连接数据库

db = pymysql.connect(host = 'localhost',port = 3306,user = 'root',
                     password = '123456',database = 'books',
                     charset ='utf8')

#获取游标(操作数据库,执行sql语句,得到执行结果)
cur = db.cursor()

#执行语句
sql = "insert into books values (5,'你的名字','铁憨憨',20,'2019-8-9','null','广大出版社','null');"
cur.execute(sql)  #执行语句

#提交到数据库
db.commit()

#关闭游标
cur.close()

#关闭数据库
db.close()