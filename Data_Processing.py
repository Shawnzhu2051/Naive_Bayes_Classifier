import re
import string

class Data_Processing(object):

    def process(self,path):
        flie = open(path,'rw')
        List = []
        Result = []
        count = 0
        # Put raw data into list
        while 1:
            line = flie.readline()
            if not line:
                break
            List.append(line)

        # find the text and process
        for line in List:
            raw = line
            raw_text = raw.split(',')[1]
            text = raw_text[3:-1]
            text = text.lower()
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
                if not(len(item) < 3 or item == 'and' or item == 'for' or item == 'the' or item == 'with' or item == 'are' or item =='not' or item == 'this' or item == 'that' or item == 'was' or item == 'were'):
                    result.append(item)
            Result.append(result)
        return Result