import csv
import re
import pandas as pd
import time

class TweetsSummary:
    def __init__(self):
        # self.tweets_csv = 
        # self.summary_csv = 
        self.data = {}
        self.summaryResult = {}
        #data = { date: { "mention": [], "hashtag": [], "website": [] } }

    def parseData(self):
        with open('tweets.csv', 'r', newline='', encoding='utf-8') as f:
            tweetsReader = csv.DictReader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in tweetsReader:
                date = row['timestamp'][:7] #YYYY-MM
                text = row['text']

                if text == "":
                    continue

                if date not in self.data:
                    #self.data[date] = {'hashtag': {}, 'website': {}, 'mention': {}}
                    self.data[date] = {"hashtag": list(), "website": list(), "mention": list()}
                else:
                    hashtags = re.finditer(r"#(?!bitcoin|btc)[^\s±§!@#$%^&*()=+.\/,:;\[\]\{\}'\"?><|\\]+", text, re.IGNORECASE)
                    tmpHash = []
                    for tag in hashtags:
                        tmpHash.append(tag.group())
                    self.data[date]["hashtag"].extend(tmpHash)

                    tmpWeb = []
                    websites = re.finditer(r'(https?:\/{2}([a-zA-Z0-9.]+\.?)(\/?\w+))', text)
                    for web in websites:
                        tmpWeb.append(web.group(2))
                    self.data[date]["website"].extend(tmpWeb)
                    
                    tmpMen = []
                    mentions = re.finditer(r'\B\@([\w\-]+)', text)  
                    for men in mentions:
                        tmpMen.append(men.group())
                    self.data[date]["mention"].extend(tmpMen)
                    
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
                    final["Website"] = pd.Series.mode(self.data[date]["website"]).iloc[0]
                else:
                    final["Website"] = "None"
                    
                writer.writerow(final)



if __name__ == "__main__":
    tweets_obj = TweetsSummary()
    start_time = time.time()
    tweets_obj.parseData()
    print(f"{(time.time() - start_time)} seconds")
    # tweets_obj.getTweetsSummary() # creates result csv file


