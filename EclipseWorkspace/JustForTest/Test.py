#coding=utf-8


strby="1,2,4\n5,6,7\n"

for items in strby.split('\n'):
    print items
    if items=='':
        continue;
    result=items.split(',')
    print result[1]
    