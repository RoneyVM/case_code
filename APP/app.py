# coding: utf-8

import tweepy

chave_consumidor = '3qflUEPUjbynZ1aeYB0uY6coj'
segredo_consumidor = 'NYoobLMgsmqetfvaMt0QpEglqwBrqobyhtVMl03vJOS8bsQX03'
token_acesso = '294453565-N101D5Gix7jJYLmk5dX3PAXCFPQG9HXd8I5klHyt'
token_acesso_segredo = '6h4gLKJTP1zQgFVzyr1YYlWZg4zY1pMByaJlnT9KBw7KM'

# Authenticate to Twitter
auth = tweepy.OAuthHandler("3qflUEPUjbynZ1aeYB0uY6coj", "NYoobLMgsmqetfvaMt0QpEglqwBrqobyhtVMl03vJOS8bsQX03")
auth.set_access_token("294453565-N101D5Gix7jJYLmk5dX3PAXCFPQG9HXd8I5klHyt", "6h4gLKJTP1zQgFVzyr1YYlWZg4zY1pMByaJlnT9KBw7KM")

# Create API object
api = tweepy.API(auth)

# Create a tweet
resultados = api.update_status("Hello Tweepy")
		
				
twitter = tweepy.API(autenticacao)

twitter.search(q='AluraOnline')

#resultados = twitter.search(q='AluraOnline')
#for tweet in resultados:
#     print(f'Usuário: {tweet.user.screen_name} - Tweet: {tweet.text}');		



