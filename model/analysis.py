import jieba
import numpy as np
import flask
from flask import render_template
import re
import nltk

#!/usr/bin/env python
#coding=utf-8
def main(article1, article2):
    remove_emoji(article1)
    remove_emoji(article2)
    seg_list1 = list(jieba.cut(article1,cut_all=False))
    seg_list2 = list(jieba.cut(article2, cut_all=False))
    
    dicts = set(seg_list1)
    dicts.update(seg_list2)

    seg_list1_wordvec = []
    seg_list2_wordvec = []
    
    if '\r\n' in dicts:
        dicts.remove('\r\n')
    for key in dicts:
        seg_list1_wordvec.append(seg_list1.count(key))
        seg_list2_wordvec.append(seg_list2.count(key))

    np1_array = np.array(seg_list1_wordvec)
    np2_array = np.array(seg_list2_wordvec)

    dot = np.dot(np1_array, np2_array)

    np1_array_sqrt = np.sqrt(np.sum(np1_array**2))
    np2_array_sqrt = np.sqrt(np.sum(np2_array**2))

    result = dot / (np1_array_sqrt * np2_array_sqrt)
    return  render_template('ans.html', cosans = str(result), dict = str(dicts), article1 = article1, article2= article2, diversity1 = diversity(article1), diversity2=diversity(article2))

def remove_emoji(string):
    emoji_pattern = re.compile("["
                         
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U00002702-\U000027B0"
                u'\U00010000-\U0010ffff'
                u"\u200d"
                u"\u2640-\u2642"
                u"\u2600-\u2B55"
                u"\u23cf"
                u"\u23e9"
                u"\u231a"
                u"\u3030"
                u"\ufe0f"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def diversity(article):
    single = nltk.text.Text(jieba.cut(article))
    return len(set(single))/len(single)