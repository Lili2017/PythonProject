#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

command = raw_input('>>')
if command=='a'
    print 'aa'
# 打开数据库连接
db = MySQLdb.connect("localhost","root","lilitju","testfirest" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM lilitju" 
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      print row[0]
      print row[1]
      print row[2]
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
db.close()