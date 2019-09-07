#-*-coding:utf-8-*-
'''
item cf main algo
'''
import reader as rd
import math
import operator


def base_contribute():
    return 1


def cal_item_sim(user_prefer):
    '''
    cal item similarity
    :param user_prefer:
    :return:
    dict,key:itemid_i ,value:dict,value_key:itemid_j,value_value:sim
    '''

    item_user_click_times = {}
    co_appear={}
    for user,itemlist in user_prefer.items():
        for index_i in range(0,len(itemlist)):
            itemid_i = itemlist[index_i]
            item_user_click_times.setdefault(itemid_i,0)
            item_user_click_times[itemid_i] += 1
            for index_j in range(index_i+1,len(itemlist)):
                itemid_j =itemlist[index_j]
                co_appear.setdefault(itemid_i,{})
                co_appear[itemid_i].setdefault(itemid_j,0)
                co_appear[itemid_i][itemid_j]+=base_contribute()

                co_appear.setdefault(itemid_j,{})
                co_appear[itemid_j].setdefault(itemid_i,0)
                co_appear[itemid_j][itemid_i] +=base_contribute()

    item_sim_score = {}
    item_sim_score_sorted ={}

    for itemid_i,related_items in co_appear.items():
        for itemid_j,co_time in related_items.items():
           sim_score = co_appear[itemid_i][itemid_j]/math.sqrt(item_user_click_times[itemid_i]*item_user_click_times[itemid_j])
           item_sim_score.setdefault(itemid_i,{})
           item_sim_score[itemid_i].setdefault(itemid_j,0)
           item_sim_score[itemid_i][itemid_j]=sim_score

    #对相似度进行排序
    for itemid in item_sim_score:
        item_sim_score_sorted[itemid] = sorted(item_sim_score[itemid].items(),key = \
                                               operator.itemgetter(1), reverse=True)

    return (item_sim_score,item_sim_score_sorted)


def cal_recom_result(sim_info,sim_info_sorted,user_prefer,movie_info):
    '''

    :param sim_info:
    :param user_prefer:
    :return:
    '''
    topk =5
    recom_info = {}
    for user in user_prefer:
        for movieid in  movie_info.keys():
            recom_info.setdefault(user, {})
            recom_info[user].setdefault(movieid, 0)
            for itemid in sim_info_sorted[movieid][0:topk][0]:
                if itemid not in user_prefer[user]:
                     continue
                recom_info[user][movieid] +=sim_info[movieid][itemid]

    return recom_info






def main_flow():
    rating_path = "../data/ml-latest-small/ratings.csv"
    movies_path = "../data/ml-latest-small/movies.csv"
    user_prefer = rd.get_user_prefer(rating_path)
    movies_info = rd.get_item_info(movies_path)
    #计算物品相似度矩阵
    (sim_info,sim_info_sorted) = cal_item_sim(user_prefer)
    recom_result = cal_recom_result(sim_info,sim_info_sorted,user_prefer,movies_info)
    print(recom_result[1.0])


if __name__ == "__main__":
    main_flow()

