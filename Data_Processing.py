#coding:utf-8
import re
import string

class Data_Processing(object):
    def process(self,path):
        uesless_word = ['and','for','the','with','are','not','this','that','was','were','these','has','there','will','have','been']
        flie = open(path,'rw')
        List = []
        Result = []
        count = 0
        #将原始数据按行分割放入一个list中
        while 1:
            line = flie.readline()
            if not line:
                break
            List.append(line)
        #处理数据
        for line in List:
            raw = line
            raw_text = raw.split(',')[1]
            text = raw_text[3:-1]
            text = text.lower()
            #根据空格来分割每个句子
            space = text.split(' ')
            result = []
            temp = []
            for item in space:
                item = item.translate(None,string.punctuation)
                if re.match(r'#',item):
                    item = item[1:]
                if not(re.search('^http',item) or re.search('^@',item)):
                    temp.append(item)
            for item in temp:
                if not(len(item) < 3 or len(item) > 15 or item in uesless_word) and str.isalpha(item):
                    result.append(item)
            Result.append(result)
        return Result