from credentials import *
import twitter

def gettimeline():
	api = twitter.Api(consumer_key=myconsumerkey,
		consumer_secret=myconsumersecret,
		access_token_key=myaccesstokenkey,
		access_token_secret=myaccesstokensecret)
	print [i.text for i in api.GetUserTimeline(count=200)]

gettimeline()