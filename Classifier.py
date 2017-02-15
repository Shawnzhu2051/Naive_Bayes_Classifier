from __future__ import division

class Classifier(object):
    def classifier(self,list):
        count = 0
        feq_table = {}
        for line in list:
            for word in line:
                count = count + 1
                if not (word in feq_table):
                    feq_table[word] = 1
                else:
                    feq_table[word] = feq_table[word] + 1
        for item in feq_table:
            temp1 = feq_table[item]
            temp2 = temp1/count
            feq_table[item] = temp2
        table = sorted(feq_table.items(),lambda x,y:cmp(x[1],y[1]), reverse= True )
        return table

    def counting(self,list):
        count = 0
        for line in list:
            for word in line:
                count = count + 1
        return count