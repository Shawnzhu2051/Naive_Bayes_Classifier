#coding:utf-8
from __future__ import division
import Data_Processing
import Classifier
import Cluster
import math


class Naive_Bayes(object):
    def __init__(self):
        self.data_processing = Data_Processing.Data_Processing()
        self.statistics = Classifier.statistics()
        self.cluster = Cluster.Cluster()

    def pretraining(self,train_resource):
    #数据预处理
        list = self.data_processing.process(train_resource)
        #counting = self.classifier.counting(list)
        #print counting
        return list

    def main_statistics(self,list):
    #统计每个分词出现的频率
        table = self.statistics.statistics(list)
        return table

    def training(self,table1,table2,positive_number):
    #训练分类器
        Conditional_probability = {}
        flag = 0
        #对两个频次表中的相同项,获取其频率作为先验概率,对于不相同的项目,加入拉普拉斯平滑系数
        for (key1,value1) in table1:
            for (key2,value2) in table2:
                if key1 == key2:
                    Conditional_probability[key1] = value2 + 1/news_number + 2
                    flag = 1
            if flag == 1:
                flag = 0
            else:
                Conditional_probability[key1] = 1/(news_number+2)
        return Conditional_probability

    def classifier(self,PN,PJ,pwiN,pwiJ,target_list):
    #输入所有的参数进行分类分类
        logs = 0
        J = 0
        N = 0
        total_TP = 0
        correct_number = 0
        for line in target_list:
            #计算总数
            total_TP = total_TP + 1
            #贝叶斯公式
            for word in line:
                if word in pwiJ:
                    J = pwiJ[word]
                else:
                    J = 1
                if word in pwiN:
                    N = pwiN[word]
                else:
                    N = 1
                logs = logs + math.log(J/N)
            D = math.log(PJ/PN) + logs
            if D < 0:
                correct_number = correct_number + 1
            logs = 0
        #正确的个数/总数,可以理解为是查全率
        rate = correct_number/total_TP
        return rate

if __name__ == "__main__":
    total_number = 139461
    news_number = 51789
    junks_number = 87663
    news_path = 'training_news_2.txt'
    junks_path = 'training_junks_2.txt'
    test_news_path = 'test_news_2.txt'
    test_junks_path = 'test_junks_2.txt'

    #Laplacian smoothing 拉普拉斯平滑
    PN = news_number + 1/total_number + 2
    PJ = junks_number + 1/total_number + 2

    obj_Naive_Bayes = Naive_Bayes()

    #数据清洗,预处理
    news_list = obj_Naive_Bayes.pretraining(news_path)
    junks_list = obj_Naive_Bayes.pretraining(junks_path)

    #根据清洗好的数据生成频次表
    news_table = obj_Naive_Bayes.main_statistics(news_list)
    junks_table = obj_Naive_Bayes.main_statistics(junks_list)

    #训练分类器,计算其中所需要的参数,先验概率等
    pwiJ = obj_Naive_Bayes.training(news_table,junks_table,news_number)
    pwiN = obj_Naive_Bayes.training(junks_table,news_table,junks_number)


    #以下是测试


    test_news_list = obj_Naive_Bayes.pretraining(test_news_path)
    news_correct_rate = obj_Naive_Bayes.classifier(PN,PJ,pwiN,pwiJ,test_news_list)
    test_junks_list = obj_Naive_Bayes.pretraining(test_junks_path)
    junks_wrong_rate = obj_Naive_Bayes.classifier(PN,PJ,pwiN,pwiJ,test_junks_list)
    junks_correct_rate = 1 - junks_wrong_rate

    print('------------------------------------')
    print('News Correct Rate 新闻分类正确的概率:')
    print(news_correct_rate)
    print('Junks Correct Rate 非新闻分类正确的概率:')
    print(junks_correct_rate)
    print('Precision 查准率:')
    print(news_correct_rate/(news_correct_rate + junks_wrong_rate))
    print('Recall 查全率:')
    print(news_correct_rate)
    print('------------------------------------')
    print('finish')