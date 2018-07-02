# coding: utf-8

import tweepy
from textblob import TextBlob

consumer_key = 'GsiY9XpLDb8pzNh8LYnf76cB6'
consumer_secret = 'XD9hoWbA18jcAsiGDKmim3QvFDUqf1X2hmpN04GlJEfdNkSl57'

access_token = '988151923508379650-vzfBQQeIB66Ve7YJMyZR0psmaZWyBLJ'
access_token_secret  = 'omEWHEi1HjGADyFbWdHO7nTCIiokrogISh5sCje6B8gqT'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search = str(input("Put what you want to search on twitter : "))
tweets = api.search(search) 

for tweet in tweets:
    print(tweet.text)
    sent = TextBlob(tweet.text)
    sentiment = sent.sentiment.polarity
    print("polarity : "+str(sentiment)+'\n')

