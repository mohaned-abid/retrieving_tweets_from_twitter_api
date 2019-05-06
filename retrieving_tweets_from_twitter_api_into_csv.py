import tweepy
from textblob import*
import numpy as np
import pandas as pd 
#step1 authentificate
consumer_key='dfu7HTI8jnojGyggBqczz8Exe'
consumer_secret='Fwsk6b1OyAdbJx4Fvt1B8MLTEUU764HBgimPyhttoPTZ2h4e3Z'
access_token='1085983267545853952-zBifShRAK4r84f1YBmE37R3AbJ53wx'
access_token_secret='b6KySoRdD7NUFOJiqrvzNdYOEfEu6GnIzDCzxbc5JlvTl'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
#deciding on the subject
chh=input('what do  u wanna discuss?')
#step2 retrive tweets
public_tweets=api.search(chh,count=100)
l=[]
for tweet in public_tweets:
    analysis=TextBlob(tweet.text)
    pol=analysis.sentiment.polarity
    obj=analysis.sentiment.subjectivity
    a2=tweet.text
    if pol<0:
        mn='negative'
    else:
        mn='positive'
    l.append([str(a2),mn])
#step3 creating our csv file
ar=np.array(l)
arr=pd.DataFrame(ar)
arr.columns=["comment","sentiment"]
arr.to_csv('mydf.csv')
