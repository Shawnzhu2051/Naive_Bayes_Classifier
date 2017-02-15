import Data_Processing
import Classifier

class Naive_Bayes(object):
    def __init__(self):
        self.data_processing = Data_Processing.Data_Processing()
        self.classifier = Classifier.Classifier()


    def training(self,train_resource):
        list = self.data_processing.process(train_resource)
        news_table = self.classifier.classifier(list)
        news_counting = self.classifier.counting(list)
        return news_table


    def output_train_result(self,table):
        for item in table:
            print(item)

if __name__ == "__main__":
    news_path = 'training_news_2.txt'
    junks_path = 'training_junks_2.txt'

    obj_Naive_Bayes = Naive_Bayes()

    news_table = obj_Naive_Bayes.training(news_path)
    junks_table = obj_Naive_Bayes.training(junks_path)

    #news_library = obj_Naive_Bayes.output_train_result(news_table)
    #junks_library = obj_Naive_Bayes.output_train_result(junks_table)

    print('finish')