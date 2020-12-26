import csv
import re
import numpy as np

# web = re.compile(r'(https?:{1}\/{2}(www\.|([a-zA-Z])+)(\.com))')
# user = re.compile(r'#bitcoin|#btc')


class TweetsSummary:
    def __init__(self):
        self.data = {}
        #data = {date: { mention: {@: count(int)},  hashtag: {#: count(int)},  website: {http/s: count(int)} } }

    def parseData(self):
        with open('tweets_small_data.csv', 'r', newline='', encoding='utf-8') as f:
            tweetsReader = csv.DictReader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in tweetsReader:
                date = row['timestamp'][:7]
                text = row['text']

                if text == "":
                    continue

                if date not in self.data:
                    # self.data[date] = {'mention': {}, 'hashtag': {}, 'website': {}}
                    self.data[date] = {'hashtag': {}, 'website': {}, 'mention': {}}

                hashtags = re.findall(r"#(?!bitcoin|btc)[^\s±§!@#$%^&*()=+.\/,:;\[\]\{\}'\"?><|\\]+", text, re.IGNORECASE)
                for tag in hashtags:
                    if tag not in self.data[date]['hashtag']:
                        self.data[date]['hashtag'][tag] = 1
                    else:
                        self.data[date]['hashtag'][tag] += 1

                websites = re.findall(r'(https?:{1}\/{2}(www\.([a-zA-Z])+)(\.))', text)
                for web in websites:
                    if web not in self.data[date]['website']:
                        self.data[date]['website'][web] = 1
                    else:
                        self.data[date]['website'][web] += 1

                mentions = re.findall(r'@([\w\-]+)', text)
                for mention in mentions:
                    if mention not in self.data[date]['mention']:
                        self.data[date]['mention'][mention] = 1
                    else:
                        self.data[date]['mention'][mention] += 1

       

    def getTweetsSummary(self):
        print(self.data.items())



if __name__ == "__main__":
    tweets_obj = TweetsSummary()
    # tweets_obj.getTweetsSummary() # creates result csv file
    tweets_obj.parseData()
    tweets_obj.getTweetsSummary()

