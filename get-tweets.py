'''
This will go through and get your most recent tweets
'''

from credentials import *
import twitter

def gettweets():
	api = twitter.Api(consumer_key=myconsumerkey,
		consumer_secret=myconsumersecret,
		access_token_key=myaccesstokenkey,
		access_token_secret=myaccesstokensecret)
	print [i.text for i in api.GetUserTimeline()]

gettweets()