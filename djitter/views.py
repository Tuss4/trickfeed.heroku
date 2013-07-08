from twitter import *
import json
from django.shortcuts import *
from django.http import *
from django.template import *
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import trickhero.settings

def djeets(request):
	oauth = OAuth1(T_CKEY, client_secret=T_CSECRET)
	request_token_url='https://api.twitter.com/oauth/request_token'
	r = requests.post(url=request_token_url, auth=oauth)
	credentials = parse_qs(r.content)
	resource_owner_key = credentials.get('oauth_token')[0]
	resource_owner_secret = credentials.get('oauth_token_secret')[0]
	authorize_url = 'https://api.twitter.com/oauth/authorize?oauth_token='
	authorize_url += authorize_url + resource_owner_key
	return HttpResponseRedirect(authorize_url)

