from django.http import *
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import *
import gdata.youtube
import gdata.youtube.service
from favo.forms import AddFav

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