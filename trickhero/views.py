from django.http import *
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import *
import gdata.youtube
import gdata.youtube.service
from favo.forms import AddFav
from django.contrib import auth
from django.contrib.auth.models import User
from trickhero.forms import New_user

def trick(request):
	a = []
	tf_user = request.user.is_authenticated()
	form = AddFav(request.POST)
	def GetAndPrintVideoFeed(uri):
		yt_service = gdata.youtube.service.YouTubeService()
		feed = yt_service.GetYouTubeVideoFeed(uri)
		for entry in feed.entry:
			for thumbnail in entry.media.thumbnail:
				t = []
				t.append(thumbnail.url)
			a.append("<a onclick=changeThisId('"+entry.media.player.url[32:43]+"')><img src="+t[0]+" alt='"+entry.media.title.text+"' title='"+entry.media.title.text+"' /></a>")
	datafeed = "http://gdata.youtube.com/feeds/api/videos?q=tricking&orderby=published&category=tricking&max-results=30"
	GetAndPrintVideoFeed(datafeed)
	return render(request, 'feed.html', {'content': a, 'form': form, 'user': tf_user})

def hi(request):
	return render(request, "login.html")

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

def register(request):
	user = User.objects.create_user(username=request.POST.get('username'),
		password=request.POST.get('password'),
		email=request.POST.get('email'))
	user.is_staff = False
	user.is_superuser = False
	user.is_active = True
	user.save()
	return HttpResponse("<a href='/login/'>Registration Successful!</a>")