#coding=utf-8
'''
Created on 2017年6月27日

@author: LIli
'''
import xlwt;
import xlrd;
#import xlutils;
from xlutils.copy import copy;
bk = xlrd.open_workbook(r"C:\Users\LIli\Desktop\testsource.xls")
w = copy(bk)
sh = bk.sheet_by_index(0)
nrows=sh.nrows
ncols = sh.ncols
w.get_sheet(0).write(nrows,0,"foo")
w.get_sheet(0).write(nrows,1,"678")
w.save(r"C:\Users\LIli\Desktop\testobjece.xls")