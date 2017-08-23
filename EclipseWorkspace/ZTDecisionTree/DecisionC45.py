#coding=utf-8
'''
Created on 2017��6��18��

@author: LIli
'''
from math import log
import operator
import uniout
import TreePlot 


def calcShannonEnt(dataSet):  # 计算数据的熵(entropy)
    numEntries=len(dataSet)  # 数据条数
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1] # 每行数据的最后一个字（类别）
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1  # 统计有多少个类以及每个类的数量
    shannonEnt=0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries # 计算单个类的熵值
        shannonEnt-=prob*log(prob,2) # 累加每个类的熵值
    return shannonEnt

def createDataSet1():    # 创造示例数据
    dataSet = [['ll', 'big', 'woman'],
               ['ss', 'big', 'man'],
               ['ll', 'big', 'man'],
               ['ll', 'small', 'maybe'],
               ['ss', 'small', 'linda'],
               ['ss', 'big', 'man'],
               ['ll', 'big', 'woman'],
               ['ll', 'big', 'woman']]
    labels = ['hair','voice']  #两个特征
    return dataSet,labels

def splitDataSet(dataSet,axis,value): # 按某个属性某个特征分类后的数据
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec =featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

#选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):  
    numFeatures = len(dataSet[0])-1  #求属性的个数
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1  
    for i in range(numFeatures):  #求所有属性的信息增益
        featList = [example[i] for example in dataSet]  
        uniqueVals = set(featList)  #第i列属性的取值（不同值）数集合
        newEntropy = 0.0  
        splitInfo = 0.0;
        for value in uniqueVals:  #求第i列属性每个不同值的熵*他们的概率
            subDataSet = splitDataSet(dataSet, i , value)  
            prob = len(subDataSet)/float(len(dataSet))  #求出该值在i列属性中的概率
            newEntropy += prob * calcShannonEnt(subDataSet)  #求i列属性各值对于的熵求和
            splitInfo -= prob * log(prob, 2);
        infoGain = (baseEntropy - newEntropy) / splitInfo;  #求出第i列属性的信息增益率
        #print infoGain;    
        if(infoGain > bestInfoGain):  #保存信息增益率最大的信息增益率值以及所在的下表（列值i）
            bestInfoGain = infoGain  
            bestFeature = i  
    return bestFeature  


def majorityCnt(classList):    #按分类后类别数量排序，比如：最后分类为2男1女，则判定为男；
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList=[example[-1] for example in dataSet]  # 类别：男或女
    if classList.count(classList[0])==len(classList):
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet) #选择最优特征
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}} #分类结果以字典形式保存
    del(labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet\
                            (dataSet,bestFeat,value),subLabels)
    return myTree



if __name__=='__main__':
    dataSet, labels=createDataSet1()  # 创造示列数据
    mytree=createTree(dataSet, labels)  # 输出决策树模型结果
    print mytree
    TreePlot.createPlot(mytree)