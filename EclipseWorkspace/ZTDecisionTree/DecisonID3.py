#coding=utf-8
'''
Created on 2017��6��18��

@author: LIli
'''
from math import log
import operator
import uniout
import TreePlot

#整个数据的熵是按照最终属性划分
#单个属性的熵是由所有取值的值按照概率累加
#单个属性的信息增益为上述二者的差

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

def createDataSet():

    dataSet = [['ll', 'lulu', 'yes'],

               ['ll', 'lulu', 'yes'],

               ['ll', 'tata', 'no'],

               ['yy', 'lulu', 'no'],

               ['yy', 'lulu', 'no']]

    labels = ['no surfacing','flippers']

    #change to discrete values

    return dataSet, labels



def splitDataSet(dataSet, axis, value):

    retDataSet = []

    for featVec in dataSet:

        if featVec[axis] == value:

            reducedFeatVec = featVec[:axis]     #chop out axis used for splitting

            reducedFeatVec.extend(featVec[axis+1:])

            retDataSet.append(reducedFeatVec)
    return retDataSet
    

def chooseBestFeatureToSplit(dataSet):

    numFeatures = len(dataSet[0]) - 1      #the last column is used for the labels

    baseEntropy = calcShannonEnt(dataSet)

    bestInfoGain = 0.0; bestFeature = -1

    for i in range(numFeatures):        #iterate over all the features

        featList = [example[i] for example in dataSet]#create a list of all the examples of this feature

        uniqueVals = set(featList)       #get a set of unique values

        newEntropy = 0.0

        for value in uniqueVals:

            subDataSet = splitDataSet(dataSet, i, value)

            prob = len(subDataSet)/float(len(dataSet))

            newEntropy += prob * calcShannonEnt(subDataSet)     

        infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy

        if (infoGain > bestInfoGain):       #compare this to the best gain so far

            bestInfoGain = infoGain         #if better than current best, set to best

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

    classList = [example[-1] for example in dataSet]

    if classList.count(classList[0]) == len(classList): 

        return classList[0]#stop splitting when all of the classes are equal

    if len(dataSet[0]) == 1: #stop splitting when there are no more features in dataSet

        return majorityCnt(classList)

    bestFeat = chooseBestFeatureToSplit(dataSet)

    bestFeatLabel = labels[bestFeat]

    myTree = {bestFeatLabel:{}}

    del(labels[bestFeat])

    featValues = [example[bestFeat] for example in dataSet]

    uniqueVals = set(featValues)

    for value in uniqueVals:

        subLabels = labels[:]       #copy all of labels, so trees don't mess up existing labels

        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)

    return myTree    






if __name__=='__main__':
    dataSet, labels=createDataSet()  # 创造示列数据
    mytree=createTree(dataSet, labels)  # 输出决策树模型结果
    print mytree
    TreePlot.createPlot(mytree)