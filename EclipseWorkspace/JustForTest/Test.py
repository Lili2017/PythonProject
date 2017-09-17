#coding=utf-8
import numpy as np
import xlrd
import xlwt
import os
from xlutils.copy import copy
from xlwt.ExcelFormulaLexer import false_pattern

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def CreateExcel(wrirefilename):
    print os.path.exists(writefilename)
    if os.path.exists(writefilename)==False:
        nwxlbook = xlwt.Workbook(encoding = 'utf-8')   #creat a xlbook object
        sheet1 = nwxlbook.add_sheet('dregister')
        sheet1.write(0,0,'时间')
        sheet1.write(0,1,'试验阶段')
        sheet1.write(0,2,'角速度平均')
        sheet1.write(0,3,'角速度3')
        sheet1.write(0,4,'角速度峰峰值')
        sheet1.write(0,5,'电机电流平均')
        sheet1.write(0,6,'电机电流3')
        sheet1.write(0,7,'电机电流峰峰值')
        sheet1.write(0,8,'平衡轮电流平均')
        sheet1.write(0,9,'平衡轮电流3')
        sheet1.write(0,10,'平衡轮电流峰峰值')
        sheet1.write(0,11,'平衡轮转速平均')
        sheet1.write(0,12,'平衡轮转速峰峰值')
        nwxlbook.save(writefilename)
        print 'newx'
    else:
        print 'none'
        
if __name__=='__main__':
    excelname=r'C:\Users\LIli\Desktop\测试.xls'
    writefilename = unicode(excelname,"utf8")
    CreateExcel(writefilename)
   
    