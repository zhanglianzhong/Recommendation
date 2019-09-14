#-*-coding:utf-8-*-
'''
author:zhanglianzhong
date:20190907
'''

import os
import pandas as pd

def get_item_info(input_file):
    '''
    get item info
    Args:
    input_file: input file path
    return: a dict. key itemId,value [title,genres]
    '''
    if not os.path.exists(input_file):
        return {}
    df = pd.read_csv(input_file)
    result = {}
    for index,line in df.iterrows():
        if len(line)<3:
            continue
        [itemId,title,genres] = line
        itemId = float(itemId)
        if itemId not in result.keys():
            result[itemId]=[title,genres]

    return result



def get_average_score(input_file):
    '''
    get every item average score
    Args:
    input_file: input file path
    return: a dict. key itemId,value average score.
    '''
    record_dict = {}
    average_score ={}
    if not os.path.exists(input_file):
        return {}
    df = pd.read_csv(input_file)
    for index,line in df.iterrows():
        movieId = line['movieId']
        if movieId not in record_dict.keys():
            record_dict[movieId]=[0,0]
        record_dict[movieId][0] +=1
        record_dict[movieId][1] +=line['rating']

    for movieId in record_dict:
        average_score[movieId]=round(record_dict[movieId][1]/record_dict[movieId][0],3)

    return average_score


def get_train_data(input_file):
    '''
    get train data
    Args:
    input_file: ratings file path
    return: a list [(userid,itemid,lable),(, ,)]
    '''
    if not os.path.exists(input_file):
        return []
    neg_dict = {}
    pos_dict = {}
    threshold = 4
    train_data =[]
    average_score = get_average_score(input_file)
    ratings_data = pd.read_csv(input_file)
    for index,line in ratings_data.iterrows():
        userid,itemid,rating = line['userId'],line['movieId'],line['rating']
        if userid not in pos_dict:
            pos_dict[userid] =[]
        if userid not in neg_dict:
            neg_dict[userid] =[]
        #如果大于阈值，给lable 1。否则，给0，这里存储的是平均分
        if rating >= threshold:
            pos_dict[userid].append((itemid,1))
        else:
            score = average_score[itemid]
            neg_dict[userid].append((itemid,score))

    #正负样本均衡和负采样
    for userid in pos_dict:
        data_num = min(len(pos_dict[userid]),len(neg_dict[userid]))
        if data_num > 0:
            train_data += [(userid,zuhe[0],zuhe[1]) for zuhe in pos_dict[userid][0:data_num]]
        else:
            continue
        sorted_neg_list = sorted(neg_dict[userid],key=lambda element:element[1],reverse=True)[0:data_num]
        train_data += [(userid,zuhe[0],0 ) for zuhe in sorted_neg_list]

    return train_data







if __name__ == '__main__':
    movies_file ='../data/ml-latest-small/movies.csv'
    ratings_file ='../data/ml-latest-small/ratings.csv'
    item_info = get_item_info(movies_file)
    average_score = get_average_score(ratings_file)
    print(item_info[1])
    print(average_score[1])
    data_train =get_train_data(ratings_file)
    print(data_train[2])

