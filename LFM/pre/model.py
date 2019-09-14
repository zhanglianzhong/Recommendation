#-*-utf8-*-
'''
LFM model train
author:zhanglianzhong
date:20190910
'''
import numpy as np


def initialParam(n):
    '''
    param n: the length of vector
    return: a list [f1,f2,...,fn]
    '''
    return np.random.rand(n)


def model_predict(user_vec, item_vec):
    length = len(user_vec)
    value = 0
    for i in range(0,length):
        value +=user_vec[i]*item_vec[i]

    return value



def train(train_data,iteTimes,alpha,F,belta):
    '''
    Args
    train_data:sample data
    iteTimes:iteration times
    alpha: train rate
    F:
    belta: regular param
    return: (user_vector,item_vector)
    '''

    user_vector = {}
    item_vector = {}
    for time in range(0,iteTimes):
        for userid,itemid,lable in train_data:
            if userid not in user_vector.keys():
                user_vector[userid] = initialParam(F)
            if itemid not in item_vector.keys():
                item_vector[itemid] = initialParam(F)
            delta = lable - model_predict(user_vector[userid],item_vector[itemid])
            for f in range(0,F):
                user_vector[userid][f] += alpha*(delta*item_vector[itemid][f]-belta*user_vector[userid][f])
                item_vector[itemid][f] += alpha*(delta*user_vector[userid][f]-belta*item_vector[itemid][f])


    return user_vector,item_vector



