#coding=utf-8
'''
Created on 2017��6��25��

@author: LIli
'''
import xlrd
import xlwt
import csv
'''
from datetime import date,datetime
import types
import time
import os
'''


#xlrd.Book.encoding = "utf-8"
def ReadExcel(filename):
    row_list=[]
    bk = xlrd.open_workbook(filename)
    try:
        sh = bk.sheet_by_index(0)
    except:
        print "读取excel出错"
    global nrows
    global ncols
    nrows=sh.nrows
    ncols = sh.ncols
    print nrows
    print ncols
#get value by row,if celltype is datetime,read it as datemode
    for i in range(0,nrows):
        row_data = sh.row_values(i)
        row_list.append(row_data)
    return row_list
        
#    for item in row_list:
#        print item[0]

def WriteExcel(writefilename,row_list):
    nwxlbook = xlwt.Workbook()   #creat a xlbook object
    sheet1 = nwxlbook.add_sheet('dregister')

    for rn in range(0,nrows):
        for cn in range(0,ncols):
            sheet1.write(rn,cn,row_list[rn][cn])# write(row,coloum,value)
    nwxlbook.save(wrfilename)


def ReadCsv(csvfilename):
    row_list2=[]
    with open(csvfilename,'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
        row_list2.append(rows)#csv一行读出来当一个元素，最后这个row_list2只有1行，row_list2[0][0]选中csv中的第一行，row_list2[0][0][0]才选中第一个元素
    return row_list2

def WriteCsv(csvobfilename,row_list2):
    with open(csvobfilename,'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row_list2[0][0])
    


if __name__ == '__main__':
    filename=r"C:\Users\LIli\Desktop\can1.xls"
    wrfilename=r"C:\Users\LIli\Desktop\cantest.xls" # if filetype ="xlsx",the object file cannot be opened
    csvfilename=r"C:\Users\LIli\Desktop\can1.csv"
    csvobfilename=r"C:\Users\LIli\Desktop\cantest.csv"
    #row_list=ReadExcel(filename)
    #WriteExcel(wrfilename)
    row_list2=ReadCsv(csvfilename)
    print len(row_list2)
    print len(row_list2[0])
    print len(row_list2[0][0])
    WriteCsv(csvobfilename,row_list2)
        
    print "done"

 
'''
python里 list可以像其他语言那样全局声明后当全局变量使用，但是普通变量不可以，必须加关键词global
'''
    


