from __future__ import division
import Data_Processing
import Classifier
import math


class Naive_Bayes(object):
    def __init__(self):
        self.data_processing = Data_Processing.Data_Processing()
        self.classifier = Classifier.Classifier()

    def pretraining(self,train_resource):
        list = self.data_processing.process(train_resource)
        #counting = self.classifier.counting(list)
        #print counting
        return list

    def statistics(self,list):
        table = self.classifier.classifier(list)
        return table

    def output_train_result(self,table):
        for item in table:
            print(item)

    def training(self,table1,table2):
        Conditional_probability = {}
        flag = 0
        for (key1,value1) in table1:
            for (key2,value2) in table2:
                if key1 == key2:
                    Conditional_probability[key1] = value2
                    flag = 1
            if flag == 1:
                flag = 0
            else:
                Conditional_probability[key1] = 1
        return Conditional_probability

    def clustering(self,PN,PJ,pwiN,pwiJ,target_list):
        logs = 0
        J = 0
        N = 0
        total_TP = 0
        correct_number = 0
        for line in target_list:
            total_TP = total_TP + 1
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
        rate = correct_number/total_TP
        return rate


if __name__ == "__main__":
    total_number = 139461
    news_path = 'training_news_2.txt'
    junks_path = 'training_junks_2.txt'
    test_news_path = 'test_news_2.txt'
    test_junks_path = 'test_junks_2.txt'
    PN = 51789/total_number
    PJ = 87663/total_number

    obj_Naive_Bayes = Naive_Bayes()

    news_list = obj_Naive_Bayes.pretraining(news_path)
    junks_list = obj_Naive_Bayes.pretraining(junks_path)

    news_table = obj_Naive_Bayes.statistics(news_list)
    junks_table = obj_Naive_Bayes.statistics(junks_list)

    pwiJ = obj_Naive_Bayes.training(news_table,junks_table)
    pwiN = obj_Naive_Bayes.training(junks_table,news_table)

    #testing!!!!!!!

    test_news_list = obj_Naive_Bayes.pretraining(test_news_path)
    news_correct_rate = obj_Naive_Bayes.clustering(PN,PJ,pwiN,pwiJ,test_news_list)
    test_junks_list = obj_Naive_Bayes.pretraining(test_junks_path)
    junks_correct_rate = obj_Naive_Bayes.clustering(PN,PJ,pwiN,pwiJ,test_junks_list)

    print('Cluster correct rate of news:')
    print(news_correct_rate)
    print('Cluster correct rate of junks:')
    print(1 - junks_correct_rate)
    #obj_Naive_Bayes.output_train_result(news_table)
    #obj_Naive_Bayes.output_train_result(junks_table)

    print('finish')