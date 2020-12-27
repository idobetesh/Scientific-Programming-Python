import csv
import re
import numpy as np
import pandas as pd

# web = re.compile(r'(https?:{1}\/{2}(www\.|([a-zA-Z])+)(\.com))')
# user = re.compile(r'#bitcoin|#btc')


class TweetsSummary:
    def __init__(self):
        self.data = {}
        #data = {date: { mention: {@: count(int)},  hashtag: {#: count(int)},  website: {http/s: count(int)} } }
        #data = {date: [mention][hashtag][website]}

    def parseData(self):
        with open('tweets.csv', 'r', newline='', encoding='utf-8') as f:
            tweetsReader = csv.DictReader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in tweetsReader:
                date = row['timestamp'][:7]
                text = row['text']

                if text == "":
                    continue

                if date not in self.data:
                    #self.data[date] = {'hashtag': {}, 'website': {}, 'mention': {}}
                    self.data[date] = {"hashtag": list(), "website": list(), "mention": list()}
                    hashtags = re.findall(r"#(?!bitcoin|btc)[^\s±§!@#$%^&*()=+.\/,:;\[\]\{\}'\"?><|\\]+", text, re.IGNORECASE)
                    for tag in hashtags:

                        self.data[date]["hashtag"].append(tag)
                    websites = re.findall(r'(https?[:/]+([A-za-z]+[.][\w]+[.]{0,1}[\w]*))', text)
                    for web in websites:
                        self.data[date]["website"].append(web)
                    mentions = re.findall(r'@([\w\-]+)', text)  
                    for men in mentions:
                        self.data[date]["mention"].append(men)

            #print(self.data)
                    
                # hashtags = re.findall(r"#(?!bitcoin|btc)[^\s±§!@#$%^&*()=+.\/,:;\[\]\{\}'\"?><|\\]+", text, re.IGNORECASE)
                # for tag in hashtags:
                #     if tag not in self.data[date]['hashtag']:
                #         self.data[date]['hashtag'][tag] = 1
                #     else:
                #         self.data[date]['hashtag'][tag] += 1
                
                # websites = re.findall(r'(https?:{1}\/{2}(www\.([a-zA-Z])+)(\.))', text)
                # for web in websites:
                #     if web not in self.data[date]['website']:
                #         self.data[date]['website'][web] = 1
                #     else:
                #         self.data[date]['website'][web] += 1

                # mentions = re.findall(r'@([\w\-]+)', text)
                # for mention in mentions:
                #     if mention not in self.data[date]['mention']:
                #         self.data[date]['mention'][mention] = 1
                #     else:
                #         self.data[date]['mention'][mention] += 1

        # print(self.data)
        self.mostFrequent()
       

    def getTweetsSummary(self):
        pass

    def mostFrequent(self):
        output_csv = "output-tweet-data.csv"
        with open(output_csv, 'w', newline='', encoding='utf-8') as f:
            header = ["Month", "Hashtag", "Mention", "Website"]
            writer = csv.DictWriter(f, header)
            writer.writeheader()
            
            for date in sorted(self.data):
                # Month,Hashtag,Mention,Website
                final = {}
                final["Month"] = date
                
                if self.data[date]["hashtag"]:
                    final["Hashtag"] = pd.Series.mode(self.data[date]["hashtag"]).iloc[0]
                else:
                    final["Hashtag"] = "None"
                    
                if self.data[date]["mention"]:
                    final["Mention"] = pd.Series.mode(self.data[date]["mention"]).iloc[0]
                else:
                    final["Mention"] = "None"

                if self.data[date]["website"]:
                    final["Website"] = pd.Series.mode(self.data[date]["website"]).iloc[0][1]
                else:
                    final["Website"] = "None"
                    
                writer.writerow(final)
            

            # result = {}
            # for date in sorted(self.data):
            #     if len(self.data[date]['mention'].values()) > 0:
            #         sorted(self.data[date]['mention'].items())
            #         a = sorted(self.data[date]['mention'].values())
            #         result[date] = {'mention': a}
            #     else:
            #         self.data[date]['mention'] = "None"
            #     if len(self.data[date]['website'].values()) > 0:
            #         b = sorted(self.data[date]['website'].values())[-1]
            #         result[date] = {'website': b}
            #     else:
            #         self.data[date]['website'] = "None"
            #     if len(self.data[date]['hashtag'].values()) > 0:
            #         c = sorted(self.data[date]['hashtag'].values())[-1]
            #         result[date] = {'hashtag': c}
            #     else:
            #         self.data[date]['hashtag'] = "None"
            # for res in result:
            #     print(res['hashtag'])
            #     print(res['website'])



if __name__ == "__main__":
    tweets_obj = TweetsSummary()
    tweets_obj.parseData()
    # tweets_obj.getTweetsSummary() # creates result csv file


