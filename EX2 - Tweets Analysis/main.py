import numpy as np
import re
import datetime as dt
import csv

web = re.compile(r'(https?:{1}\/{2}(www\.|[a-zA-Z])+\.com)')
# https?:{1}\/{2}(www\.|[a-zA-Z]+)+\.com

btc = re.compile(r'#bitcoin|#btc')


def summary(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        mySet = set()
        for row in reader:
            if btc.search(dict(row)['text'].lower()) is not None:
                #print("===========================", dict(row)['text'])
                continue
            if web.search(dict(row)['text']) is not None:
                # print("******************",dict(row)['text'])
                continue
            # mySet.add(dt.datetime.strptime(dict(row)['timestamp'][:7], '%Y-%m').date())
            mySet.add(dict(row)['timestamp'][:7])
        a = list(mySet)
        a = sorted(a)
        print(a)



if __name__ == '__main__':
    # summary("t.csv")
    summary("tweets_small_data.csv")
    # summary("tweets.csv")
