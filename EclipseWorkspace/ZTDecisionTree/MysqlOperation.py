#coding=utf-8
'''
Created on 2017��6��26��
http://www.runoob.com/python/python-mysql.html
@author: LIli
'''
import MySQLdb

# 打开数据库连接
def Connectsql(hostname,user,password,dbname):
    try:
        db = MySQLdb.connect(hostname,user,password,dbname)
        cursor = db.cursor()
        return cursor
    except Exception,e:  
        print Exception,":",e



    
    