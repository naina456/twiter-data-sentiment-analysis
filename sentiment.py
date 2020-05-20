import numpy as np  
import pandas as pd  
import re 
import csv
from matplotlib import pyplot as plt
from matplotlib import style
import seaborn as sns 
import paralleldots
paralleldots.set_api_key("lR59RnPyLqGvNMA9uQAzHRffycPlLAhhBjnXEoM28Ws ")
df= pd.read_csv('dbit.csv',header=0,encoding = 'unicode_escape') 
positive=0
negative=0
neutral=0
count=1
starting=34
tweets=[]
positiveTweets=[]
negativeTweets=[]
neutralTweets=[]
for tweet in df.tweets: 
    if count>starting:
        tweets.append(tweet)
        count+=1
        if count>starting+5:
            break
    else:
        count+=1

count=0

response=paralleldots.batch_sentiment(tweets)
for sentiment in response['sentiment']:
    print(sentiment)
    if sentiment['positive']>0.4:
        positive+=1
        positiveTweets.append(tweets[count])
    if sentiment['negative']>0.4:
        negative+=1
        negativeTweets.append(tweets[count])
    if sentiment['neutral']>0.4:
        neutral+=1
        neutralTweets.append(tweets[count])
    count+=1
print("==================")
print(str((positive/count)*100)+" % Positive Feedbacks")
print(str((negative/count)*100)+" % Negative Feedbacks")
print(str((neutral/count)*100)+" % Neutral Feedbacks")
print("==================")
# print(positiveTweets)
# print(neutralTweets)
# print(negativeTweets)


csvFile = open('sen.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
# csvWriter.writerow(['Tweet','status'])
for tweet in positiveTweets:
    print("Positive: "+ tweet)
    csvWriter.writerow([tweet.encode('utf-8'),'Positive'])
print("==================")
for tweet in negativeTweets:
    print("Negative: "+ tweet)
    csvWriter.writerow([tweet.encode('utf-8'),'Negative'])
print("==================")
for tweet in neutralTweets:
    print("Neutral: "+ tweet)
    csvWriter.writerow([tweet.encode('utf-8'),'Neutral'])
print("==================")
