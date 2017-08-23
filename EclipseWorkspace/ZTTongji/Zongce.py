#coding=utf-8
'''
Created on 2017年8月21日

@author: LIli
'''

#import pandas as pd
import numpy as np
import xlrd
import xlwt
import os
from xlutils.copy import copy

'''
def ReadOneExcel(filename,anglenum,djcurrentnum,phcurentnum,phspeednum,datetimenum,choosespeed):
    row_list=[]
    bk = xlrd.open_workbook(filename)
    try:
        sh = bk.sheet_by_index(0)
    except:
        print "读取excel出错"
    nrows=sh.nrows
    
    
    for i in range(1,nrows):
        
        angle=sh.row_values(anglenum-1)
        if (angle>choosespeed-0.5):
            
'''
def CalculateData(data):
    aver=np.mean(data)
    stdva=np.std(data,ddof = 1)
    maxval=np.max(data)
    minval=np.min(data)
    return aver,stdva,maxval,minval

#获取完整路径的文件名字
def Getfilename(filefullpath):
    filename=os.path.basename(readexcelname)
    filenamewithoutex,exten=os.path.splitext(filename)
    return filenamewithoutex

#写入excel追加方式
def WriteExcel(writefilename,name):
    f=xlrd.open_workbook(writefilename)#读取一个Excel文件到内存
    sh = f.sheet_by_index(0)
    nrow=sh.nrows
    d=copy(f)#复制表
    w=d.get_sheet(0)                   
    w.write(nrow,6,name)# write(row,coloum,value)
    os.remove(writefilename)
    d.save(writefilename)

excelname=r'C:\Users\LIli\Desktop\测试.xls'
readexcelname = unicode(excelname,"utf8")

name=Getfilename(readexcelname)
rowli=[1,2,3,4]
WriteExcel(readexcelname,name)



