from ast import If
from socket import if_indextoname
from textblob import TextBlob
import pandas as pd
import numpy as np
import re
import tweepy



def getResult(name):
    bearer_token="AAAAAAAAAAAAAAAAAAAAAIoxbQEAAAAAOOfYpI98QgVAMvP1Pz%2FZfgqsRvs%3DMiKzzculmsEXtK2Soi2nCVYfubpykt3q8FzGlm5nf8lC1nHORA"
    client = tweepy.Client(bearer_token)
    post = client.search_recent_tweets(query=name,max_results=100)
    tweets=post.data
    df=pd.DataFrame([i.text for i in tweets],columns=["Tweets"] )

    # print(df["Tweets"])


    def cleanT(text):
        text= re.sub(r"@[A-Za-z0-9]+","",text)
        text=re.sub(r"#","",text)
        text=re.sub(r"RT[\s]:+","",text)
        # text=re.sub(r"https?:\/\/\S+","  ")

        return text


    df["Tweets"]=df["Tweets"].apply(cleanT)

    # print(df["Tweets"])

    def getSubjectivity(text):
        return TextBlob(text).sentiment.subjectivity


    def getPolarity(text):
        return TextBlob(text).sentiment.polarity



    df["Subjectivity"]=df['Tweets'].apply(getSubjectivity)


    df["Polarity"]=df['Tweets'].apply(getPolarity)



    # print(df)



    #analysis

    def getAnalysis(score):
        if score<0:
            return "Negative"
        elif score==0:
            return "Neutral"
        else:
            return "Positive"


    df["Sentiments"]=df["Polarity"].apply(getAnalysis)
    l=df["Sentiments"].value_counts()
    l=l.to_json()
    return l


    