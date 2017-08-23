#coding=utf-8
'''
Created on 2017��6��26��

@author: LIli
'''
import time  

#将汉字时间转换为标准时间
def str2datetime(inputstr):
    vyear=inputstr[0:4]
    vmonth=inputstr[7:9]
    vday=inputstr[12:14]
    vhour=inputstr[18:20]
    vminute=inputstr[23:25]
    vsecond=inputstr[28:30]
    strtime= "%s-%s-%s %s:%s:%s"%(vyear,vmonth,vday,vhour,vminute,vsecond)
    timeform=time.strptime(strtime, "%Y-%m-%d %H:%M:%S");
    return timeform
    #print time.datetime(vyear,vmonth,vday,vhour,vminute,vsecond)
    
if __name__ == '__main__':
    inputstr='2017年06月07日 16时50分55秒'
    print str2datetime(inputstr)
