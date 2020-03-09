# coding: utf-8

import sys
import tweepy
import csv
import mysql.connector
import time

#Conexão com o DataBase
mydb = mysql.connector.connect(
  host="##############",
  user="##############",
  passwd="############",
  database="##########"
)
mycursor = mydb.cursor()
	
#Key / Chaves de autenticação
consumer_key = '####################################'
consumer_secret = '#################################'
access_token = '####################################'
access_token_secret = '#############################'
 
#Autenticação	
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
#Função para consulta da Hashtag no Twiter - Configurado para consulta apartir do dia INICIO do CASE 27/02/2020
def Pesq_Hashtag(Hashtag):
	#Set variavel para consulta
	HT = str(Hashtag)
	for tweet in tweepy.Cursor(api.search,q=HT,count=300,since="2020-02-20").items():
		#Set variaveis locais
		ID = tweet.id
		DATA = tweet.created_at
		USER = tweet.author._json['screen_name']
		QTD = api.get_user(USER).followers_count
		LNG = tweet.lang
		TWT = (tweet.text).encode('utf8')
		#Escreve no arquivo

		#mycursor.execute("CREATE TABLE IF NOT EXISTS tweet(id_twitter BIGINT(30),	created_at DATETIME, user VARCHAR(50), lang VARCHAR(20), followers INT(30), hashtag VARCHAR(50), tweet TEXT(280))")
		time.sleep(2)
		try:
			val = (ID, DATA, USER, LNG, QTD, HT, TWT )
			print(ID,DATA,USER,LNG,QTD,HT)
			sql = "INSERT INTO tweet(id_twitter, created_at, user, lang, followers, hashtag, tweet) VALUES (%s, %s, %s, %s, %s, %s, %s)"
			mycursor.execute(sql, val)
			mydb.commit()
		except:
			print("ERRO TWEET JA EXISTE NA BASE",ID,DATA,USER,LNG,QTD,HT)

#Função para consulta da Hashtag
Pesq_Hashtag("#devops")
Pesq_Hashtag("#openbanking")
Pesq_Hashtag("#apifirst")
Pesq_Hashtag("#devops")
Pesq_Hashtag("#cloudfirst")
Pesq_Hashtag("#microservices")
Pesq_Hashtag("#apigateway")
Pesq_Hashtag("#oauth")
Pesq_Hashtag("#swagger")
Pesq_Hashtag("#raml")
Pesq_Hashtag("#openapis")
