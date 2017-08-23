#coding=gbk
'''
Created on 2017��6��19��

@author: LIli
'''
import xlrd
import xlwt
from datetime import date,datetime
import types
import time
import os



#direction operation
file_path='datapath'
if not os.path.isdir(file_path):
    os.makedirs(file_path)


#Read excel
fname = ".\Sheet1.xlsx"
#xlrd.Book.encoding = "gbk"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
 sh = bk.sheet_by_name("Sheet1")
except:
 print "no sheet in %s named Sheet1" % fname
#get sheet row number
nrows = sh.nrows
#get sheet coloum number
ncols = sh.ncols
print "nrows %d, ncols %d" % (nrows,ncols)
#get one cell value
cell_value = sh.cell_value(0,2)
print cell_value
 
row_list = []
#get value by row,if celltype is datetime,read it as datemode
for i in range(0,nrows):
    row_data = sh.row_values(i)
    if sh.cell(i,0).ctype==3: #ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
        date_value = xlrd.xldate_as_tuple(row_data[0],bk.datemode)
        time_tmp =  datetime(*date_value[:6])
    row_list.append(row_data)
    


 
 
#write file
wrfilename=".\%s\%s"%(file_path,"sheet2.xls") # if filetype ="xlsx",the object file cannot be opened
nwxlbook = xlwt.Workbook()   #creat a xlbook object
sheet1 = nwxlbook.add_sheet('dregister')



for rn in range(0,len(row_list)):
    for cn in range(0,3):
        sheet1.write(rn,cn,row_list[rn][cn])# write(row,coloum,value)
nwxlbook.save(wrfilename)








