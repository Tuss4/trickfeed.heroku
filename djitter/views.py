from twitter import *
import json
from django.shortcuts import *
from django.http import *
from django.template import *

def djeets(request):
	t = Twitter(
		auth=OAuth('102957761-OlKsFJ5Kd2PRY5CMX6rciTsoSaElTOkvyTdAky6K','YXnpXVWV0faXWwA3yVl3cOjzkmkCg7ExvRkQ2Fdsn4',
			'P7fozjQ5eIzZNnBKivfcg','eG11PhAE9XtZvoeJfiIcy0wEvGcb0TjGzLxXoxi1Qk')		
		)

	feed = t.search.tweets(q="#tricking", result_type="recent")

	list_of_tweets = []
	for i in feed[u'statuses']:
		list_of_tweets.append(i[u'user'][u'name']+": "+i[u'text'])
	return render(request, "djeets.html", {'list': list_of_tweets})