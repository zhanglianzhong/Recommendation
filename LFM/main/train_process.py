#-*-utf8-*-
'''
author:zhanglianzhong
date:20190911
'''
import sys
from LFM.util.read import get_train_data
from LFM.pre.model import train

def train_process():
    ratings_file ='../data/ml-latest-small/ratings.csv'
    train_data = get_train_data(ratings_file)
    iterTimes = 30     #迭代次数
    F =50        #隐类因子个数
    alpha = 0.3    #步长
    belta = 0.01   #正则化参数
    user_vector,item_vector = train(train_data,iterTimes,alpha,F,belta)
    print(user_vector)
    print(item_vector)



if __name__ == '__main__':
    train_process()
