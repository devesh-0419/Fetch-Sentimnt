from textblob import TextBlob
import keys 
import pandas as pd
import numpy as np
import tweepy

# import analysis 

def getData(name):
    client = tweepy.Client(keys.bearer_token)
    post = client.search_recent_tweets(query=name,max_results=100)
    tweets=post.data
    print(tweets)
    return tweets



# name = input("enter your query")



# val=analysis.getResult(name)

# print(val.to_json())


