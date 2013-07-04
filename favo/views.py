from django.shortcuts import *
from django.http import *
from django.core.context_processors import csrf
from favo.models import Favorite

def success(request): 
	#How a user adds videos to their favorites. 
	#If the video is already saved it won't add. 
	if request.method == 'POST':
		f = Favorite(user = request.user.username,
			video = request.POST['video'])
		favorites = Favorite.objects.all()
		v = request.POST['video']
		fs = Favorite.objects.filter(video=v, user=request.user.username)
		#fu = Favorite.objects.filter(user=request.user.username)
		if fs:
			return HttpResponseRedirect("/nodice/")
		f.save()
		return HttpResponseRedirect("/myfavs/")

def list_fav(request):
	#The "my favorites" page
	if request.user.is_authenticated():
		videos = Favorite.objects.filter(user=request.user.username)
		return render(request, "favorites.html", {"videos": videos})

def edit_fav(request):
	if request.user.is_authenticated():
		vid_list = Favorite.objects.filter(user=request.user.username)
		return render(request, "edit_favorites.html", {"list": vid_list})

def del_fav(request):
	if request.method == 'POST':
		vidlist = request.POST.get("video"):
				return HttpResponse("vidlist")


