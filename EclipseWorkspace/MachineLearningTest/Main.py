#coding=utf-8
'''
Created on 2017��6��17��

@author: LIli
'''
#coding=utf-8

import numpy as np

import matplotlib.pyplot as plt

import initdata as idata



train,test=idata.load_data()

x_train, y_train = train[:,:2], train[:,2] #����ǰ������x1,x2 ��������y,�����y���������

x_test ,y_test = test[:,:2], test[:,2] # ͬ��,���������yû������







def try_different_method(clf):

    clf.fit(x_train,y_train)

    score = clf.score(x_test, y_test)

    result = clf.predict(x_test)

    plt.figure()

    plt.plot(np.arange(len(result)), y_test,'go-',label='true value')

    plt.plot(np.arange(len(result)),result,'ro-',label='predict value')

    plt.title('score: %f'%score)

    plt.legend()

    plt.show()







from sklearn import ensemble

rf =ensemble.RandomForestRegressor(n_estimators=20)

try_different_method(rf)







'''



plt.figure(1)

plt.plot(x[:,0], x[:,2],'go-',label='true value')

plt.plot(y[:,0], y[:,2],'ro-',label='true value')

plt.show()



'''



