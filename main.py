from credentials import *
import twitter


api = twitter.Api(consumer_key=myconsumerkey,
		consumer_secret=myconsumersecret,
		access_token_key=myaccesstokenkey,
		access_token_secret=myaccesstokensecret)


def gettimeline():
	return api.GetUserTimeline(count=200)

def clean_timeline(timeline):
	for i in timeline:
		if 'bad_word' in i.text:
			api.DestroyStatus(i.id)
			print "Just destroyed %d" % i.text

clean_timeline(gettimeline())
