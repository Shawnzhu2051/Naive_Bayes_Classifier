#coding:utf-8
from __future__ import division
from collections import Counter

class statistics(object):
    def statistics(self,list):
        i = 0
        table = []
        for line in list:
            for word in line:
                table.append(word)
                i = i + 1
        counter = Counter(table)
        times = counter.most_common(i)
        return times

    def counting(self,list):
        count = 0
        for line in list:
            for word in line:
                count = count + 1
        return count
