import re
import csv
import pandas as pd
import time

class TweetsSummary:
    def __init__(self):
        self.data = {}
        #tweets.csv => { YYYY-MM: { "mention": [], "hashtag": [], "website": [] } }
                     # { YYYY-MM: { "mention": [], "hashtag": [], "website": [] } }
                     # { YYYY-MM: { "mention": [], "hashtag": [], "website": [] } } ...
        

    def getTweetsSummary(self):
        ''' This function opens csv file named tweet.csv and creates a data set that looks as mention above.
            It takes the date from the 'timestamp' from each row and starts to go over the 'text' colunm 
            and search using regex expressions tofind the correct patterns
            then it adds the data to the relevant list in the current date dict.
            At the end it calls the findMostFreqAndGenCsv function '''

        with open('tweets.csv', 'r', newline='', encoding='utf-8') as source_file:
            tweetsReader = csv.DictReader(source_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for row in tweetsReader:
                date = row['timestamp'][:7] #YYYY-MM
                text = row['text']

                if text == "":
                    continue

                if date not in self.data:
                    self.data[date] = {"hashtag": [], "website": [], "mention": []}
                else:
                    hashtags = re.finditer(r"#(?!bitcoin|btc)[^\s±§!@#$%^&*()=+.\/,:;\[\]\{\}'\"?><|\\]+", text, re.IGNORECASE)
                    tmpHash = []
                    for tag in hashtags:
                        tmpHash.append(tag.group())
                    self.data[date]["hashtag"].extend(tmpHash)

                    tmpWeb = []
                    websites = re.finditer(r'https?:\/\/([A-za-z0-9]+\.[\w\-]+\.*[\w\-]*)', text)
                    for web in websites:
                        tmpWeb.append(web.group(1))
                    self.data[date]["website"].extend(tmpWeb)
                    
                    tmpMen = []
                    mentions = re.finditer(r'@([\w\-]+)', text)  
                    for men in mentions:
                        tmpMen.append(men.group())
                    self.data[date]["mention"].extend(tmpMen)
                        
            self.findMostFreqAndGenCsv()


    def findMostFreqAndGenCsv(self):
        ''' This function finds the most frequent hashtag/website/mention for every month in tweets.csv
         and generates output csv of the result using the Pandas mode functions.'''

        with open("tweet-data.csv", 'w', newline='', encoding='utf-8') as output_file:
            header = ["Month", "Hashtag", "Mention", "Website"]
            writer = csv.DictWriter(output_file, header)
            writer.writeheader()
            
            for date in sorted(self.data):
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
    start = time.time()
    tweets_obj.getTweetsSummary()
    print(f"{(time.time() - start)} seconds")


