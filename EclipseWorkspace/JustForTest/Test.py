#coding=utf-8
'''
Created on 2017年7月9日

@author: LIli
'''


from numpy import *

def binSplitDataSet(dataSet, feature, value):

    mat0 = dataSet[nonzero(dataSet[:,feature] > value)[0],:]

    mat1 = dataSet[nonzero(dataSet[:,feature] <= value)[0],:]

    return mat0,mat1
'''
a=mat(eye(4))

mat0,mat1= binSplitDataSet(a, 1,0.5)
print mat0
print mat1
'''
print power(4,2)

