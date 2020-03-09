# coding: utf-8

import sys
import tweepy
import json
import csv

#Autenticações
consumer_key = '3qflUEPUjbynZ1aeYB0uY6coj'
consumer_secret = 'NYoobLMgsmqetfvaMt0QpEglqwBrqobyhtVMl03vJOS8bsQX03'
access_token = '294453565-N101D5Gix7jJYLmk5dX3PAXCFPQG9HXd8I5klHyt'
access_token_secret = '6h4gLKJTP1zQgFVzyr1YYlWZg4zY1pMByaJlnT9KBw7KM'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,
                           lang="en",
                           since="2020-03-02").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
	