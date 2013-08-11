from django.http import *
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import *
import urllib2
import json
from favo.forms import AddFav
from django.contrib import auth
from django.contrib.auth.models import User
from trickhero.forms import New_user

def trick(request):
	a = []
	tf_user = request.user.is_authenticated()
	form = AddFav(request.POST)
	datafeed = "http://gdata.youtube.com/feeds/api/videos?q=tricking&alt=json&format=5&orderby=published&category=tricking&max-results=30"
	raw = urllib2.urlopen(datafeed)
	v_feed = json.load(raw)
	entries = v_feed['feed']['entry']
	for entry in entries:
		a.append("<a onclick=changeThisId('"+entry['id']['$t'][42:53]+"')><img src="+entry['media$group']['media$thumbnail'][0]['url']+" alt='"+entry['media$group']['media$title']['$t']+"' title='"+entry['media$group']['media$title']['$t']+"' /></a>")
	return render(request, 'feed.html', {'content': a, 'form': form, 'user': tf_user})

def hi(request):
	user = False
	return render(request, "login.html", {'user': user})

def login(request):
	errors = False
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect("/home/")
	else:
		errors = True
		return render(request, "login.html", {'errors': errors})

def logout(request):
 	auth.logout(request)
 	return HttpResponseRedirect("/home/")

def new(request):
	form = New_user
	return render(request, "register.html", {'form': form})

def nodice(request):
	fail = True
	return render(request, "feed.html", {'fail': fail})

def register(request):
	user = User.objects.create_user(username=request.POST.get('username'),
		password=request.POST.get('password'),
		email=request.POST.get('email'))
	user.is_staff = False
	user.is_superuser = False
	user.is_active = True
	user.save()
	return HttpResponseRedirect("/hello/")