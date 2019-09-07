#-*-coding:utf-8-*-
import os
import pandas as pd
'''
author:zhanglianzhong
date:20190901
'''


def get_user_click(rating_file):
    '''
    get user click list
    :param rating_file: input file
    :return: 
     dict key:userid,value:[itemid1,itemid2...]
    '''

    if not os.path.exists(rating_file):
        return {}

    result = {}
    df = pd.read_csv(rating_file)
    for index,line in df.iterrows():
        userId = line["userId"]
        if userId  not in result.keys():
           result[userId]=[]
        result[userId].append(line["movieId"])

    return result




def  get_user_prefer(rating_file):
     '''
     get user likeing list,if score big than 3,we think people like this movie.
     :param rating_file: input file
     :return: dict. key:userId,value:[itemId1,itemId2...]
     '''
     if not os.path.exists(rating_file):
         return {}
     result = {}
     df = pd.read_csv(rating_file)
     for index,line in df.iterrows():
         #评分 >=3 认为喜欢这部电影
         if line["rating"] <3:
             continue
         userId = line["userId"]
         if userId not in result.keys():
             result[userId] = []
         result[userId].append(line["movieId"])

     return result


def get_item_info(item_file):
    '''
    get item info
    :param item_file: input file
    :return: key:itemId,value:[title,genres]
    '''
    if not os.path.exists(item_file):
        return {}
    df = pd.read_csv(item_file)
    result = {}
    for index,line in df.iterrows():
        if len(line)<3:
            continue
        [itemId,title,genres] = line
        itemId = float(itemId)
        if itemId not in result.keys():
            result[itemId]=[title,genres]

    return result

