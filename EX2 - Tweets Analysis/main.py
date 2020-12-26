import numpy as np
import re
import datetime as dt
import csv

web = re.compile(r'(https?:{1}\/{2}(www\.|([a-zA-Z])+)(\.com))')
# https?:{1}\/{2}(www\.|[a-zA-Z]+)+\.com

btc = re.compile(r'#bitcoin|#btc')


def summary(csv_file):
    # data = np.genfromtxt(csv_file, delimiter=';', encoding='utf-8')
    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        reader = list(csv.reader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL))
        reader = np.array(reader[1:], dtype=np.str)
        print(reader.shape)

        mySet = set()
        myDict = {}
        for row in reader:
            if btc.search(dict(row)['text'].lower()) is not None:
                #print("===========================", dict(row)['text'])
                continue
            # if web.search(dict(row)['text']) is not None:
            tmp =  web.findall(dict(row)['text']) 
            if tmp:
                t = f"www.{tmp[0][1]}.com"
                myDict[t] = myDict.get(t, 0) + 1
                print(t)
                # print("******************",dict(row)['text'])
                continue
            # mySet.add(dt.datetime.strptime(dict(row)['timestamp'][:7], '%Y-%m').date())
            mySet.add(dict(row)['timestamp'][:7])
        a = list(mySet)
        a = sorted(a)
        print(a)
        print(myDict)



if __name__ == '__main__':
    summary("t.csv")
    # summary("tweets_small_data.csv")
    # summary("tweets.csv")
