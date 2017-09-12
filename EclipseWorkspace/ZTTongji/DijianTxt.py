#coding=utf-8
'''
Created on 2017��9��11��

@author: LIli
'''
import numpy as np
import xlrd
import xlwt
import os
from xlutils.copy import copy
from xlwt.ExcelFormulaLexer import false_pattern

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def listdir(path):
    list_name=[]  
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path)  
        elif os.path.splitext(file_path)[1]=='.txt':  
            list_name.append(file_path)
    return list_name  
        

def CalculateData(data):
    aver=np.mean(data)
    stdva=3*np.std(data,ddof = 1)
    maxval=np.max(data)
    minval=np.min(data)
    peakvalue=maxval-minval
    return aver,stdva,peakvalue  

#写入excel追加方式
def WriteExcel(writefilename,name):
    '''
    if os._exists(writefilename)==False:
        nwxlbook = xlwt.Workbook()   #creat a xlbook object
        sheet1 = nwxlbook.add_sheet('dregister')
        
        
        sheet1.write(0,0,unicode('时间',"utf8")
        sheet1.write(0,1,'试验阶段'.decode('UTF-8').encode('GBK'))
        sheet1.write(0,2,'角速度平均'.decode('UTF-8').encode('GBK'))
        sheet1.write(0,3,'角速度3'.decode('UTF-8').encode('GBK'))
        sheet1.write(0,4,'角速度峰峰值'.decode('UTF-8').encode('GBK'))
        sheet1.write(0,5,'平衡轮电流平均'.decode('UTF-8').encode('GBK'))
        sheet1.write(0,6,'平衡轮电流3'.decode('UTF-8').encode('GBK'))
        sheet1.write(0,7,'平衡轮电流峰峰值'.decode('UTF-8').encode('GBK'))
        sheet1.write(0,8,'平衡轮转速平均'.decode('UTF-8').encode('GBK'))
        sheet1.write(0,9,'平衡轮转速峰峰值'.decode('UTF-8').encode('GBK'))
        
        nwxlbook.save(writefilename)
    '''     
    f=xlrd.open_workbook(writefilename)#读取一个Excel文件到内存
    sh = f.sheet_by_index(0)
    nrow=sh.nrows
    d=copy(f)#复制表
    w=d.get_sheet(0)
    for i in range(0,len(name)):              
        w.write(nrow,i,name[i])# write(row,coloum,value)
    os.remove(writefilename)
    d.save(writefilename) 
        
 #获取完整路径的文件名字
def Getfilename(filefullpath):
    filename=os.path.basename(filefullpath)
    filenamewithoutex,exten=os.path.splitext(filename)
    return filenamewithoutex       
    
    
    
    
#Read TXTfile and extract need data
def GetdatafromTxt(txtfilefullpath,writefilename):
    experimodel=Getfilename(txtfilefullpath)
    
    timenum=1-1
    anglenum=7-1
    ztcurrentnum=14-1
    phcurrentnum=15-1
    phspeednum=16-1
    workmodalnum=6-1
    
    timelist=[]
    ztcurrentlist=[]
    anglelist=[]
    phcurrentlist=[]
    phspeedlist=[]
    
    enterstatus=False
    tempnum=1;
    
    f = open(txtfilefullpath,'r')  
    lines = f.readlines()#��ȡȫ������  
    
    
    for line in lines : 
        if '时间' in line:
            continue;
       
        tempdata=line.split(',')
        workmodal=tempdata[workmodalnum].decode("gbk").encode("utf-8")
        if '旋转' in workmodal:
            tempnum=tempnum+1
            if tempnum<20:
                continue;                
            timelist.append(tempdata[timenum])
            anglelist.append(float(tempdata[anglenum]))
            ztcurrentlist.append(float(tempdata[ztcurrentnum]))
            phcurrentlist.append(float(tempdata[phcurrentnum]))
            phspeedlist.append(float(tempdata[phspeednum]))
            enterstatus=True
            
        elif (enterstatus==True):
           
            angleaver,anglestd,anglepeak=CalculateData(anglelist)
            ztcurrentaver,ztcurstd,ztcurpeak=CalculateData(ztcurrentlist)
            phspeedaver,phspeedstd,phspeedpeak=CalculateData(phspeedlist)
            phcurrentaver,phcurrentstd,phcurrentpeak=CalculateData(phcurrentlist)
            starttime=timelist[0]      
            name=[starttime,experimodel,angleaver,anglestd,anglepeak,ztcurrentaver,ztcurstd,ztcurpeak,phcurrentaver,phcurrentstd,phcurrentpeak,phspeedaver,phspeedpeak]
            WriteExcel(writefilename,name)
            
            timelist=[]
            ztcurrentlist=[]
            anglelist=[]
            phcurrentlist=[]
            phspeedlist=[]
            
            enterstatus=False
            tempnum=1;
 
if __name__=='__main__':
    #textfilename=r'C:\Users\LIli\Desktop\dijian\remote_20179111147114.txt'
    writefilename=r'C:\Users\LIli\Desktop\07\result.xls'
    datapath=r'C:\Users\LIli\Desktop\07'
    listname=listdir(datapath)
    
    for m in range(0,len(listname)):
        print listname[m]
        GetdatafromTxt(listname[m],writefilename)
    print "done"
