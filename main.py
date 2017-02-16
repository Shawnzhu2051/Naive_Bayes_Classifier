from __future__ import division
import Data_Processing
import Classifier


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
        count = 0
        for (key1,value1) in table1:
            for (key2,value2) in table2:
                if key1 == key2:
                    Conditional_probability[key1] = value2
                    count = count + 1
        print count
        return Conditional_probability

    def clustering(self,PN,PJ,pwiN,pwiJ,target_list):
        PtJ = 1
        PtN = 1
        total_TP = 0
        correct_number = 0
        for line in target_list:
            total_TP = total_TP + 1
            for word in line:
                if word in pwiJ :
                    PtJ = PtJ * pwiJ[word]
                if word in pwiN :
                    PtN = PtN * pwiN[word]
            D = (PJ*PtJ)/(PN*PtN)
            if D <= 1:
                correct_number = correct_number + 1
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
    D1 = obj_Naive_Bayes.clustering(PN,PJ,pwiN,pwiJ,test_news_list)

    #obj_Naive_Bayes.output_train_result(news_table)
    #obj_Naive_Bayes.output_train_result(junks_table)

    print('finish')