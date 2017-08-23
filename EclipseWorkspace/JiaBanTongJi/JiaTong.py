#coding=utf-8
'''
Created on 2017���8���11���

@author: LIli
'''
from optparse import Values
'''
name=raw_input("���������")
if name=="������":
    print '������'
'''
import xlrd
import xlwt


writefilename=r'C:\Users\LIli\Desktop\result\result.xls'
readexcelname=r'C:\Users\LIli\Desktop\result\yuan.xls'
namelist=[]
status=True;


    
def nametongji():
    labelvalue={}
    namelistnon=set(namelist)
    for labelname in namelistnon:
        labelvalue[labelname]=namelist.count(labelname)
    WriteExcel(writefilename,labelvalue)
        
        
def WriteExcel(writefilename,row_list):
    nwxlbook = xlwt.Workbook()   #creat a xlbook object
    sheet1 = nwxlbook.add_sheet('dregister')
    rn=0;

    for key,value in row_list.items():
            sheet1.write(rn,0,key)# write(row,coloum,value)
            sheet1.write(rn,1,value)# write(row,coloum,value)
            rn+=1
    nwxlbook.save(writefilename)  

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
        row_data = sh.row_values(i)[0]
        row_list.append(row_data)
    return row_list 


namelist=ReadExcel(readexcelname)
nametongji()