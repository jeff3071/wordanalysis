import jieba
import numpy as np


def main(article1, article2):
    seg_list1 = list(jieba.cut(article1,cut_all=False))
    seg_list2 = list(jieba.cut(article2, cut_all=False))
    
    dicts = set(seg_list1)
    dicts.update(seg_list2)

    seg_list1_wordvec = []
    seg_list2_wordvec = []
    
    for key in dicts:
        seg_list1_wordvec.append(seg_list1.count(key))
        seg_list2_wordvec.append(seg_list2.count(key))

    np1_array = np.array(seg_list1_wordvec)
    np2_array = np.array(seg_list2_wordvec)

    dot = np.dot(np1_array, np2_array)

    np1_array_sqrt = np.sqrt(np.sum(np1_array**2))
    np2_array_sqrt = np.sqrt(np.sum(np2_array**2))

    result = dot / (np1_array_sqrt * np2_array_sqrt)

    return "Cos相似值: " + str(result)

