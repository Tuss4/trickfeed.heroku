from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
import gdata.youtube
import gdata.youtube.service

def trick(request):
	a = []
	def GetAndPrintVideoFeed(uri):
		yt_service = gdata.youtube.service.YouTubeService()
		feed = yt_service.GetYouTubeVideoFeed(uri)
		for entry in feed.entry:
			for thumbnail in entry.media.thumbnail:
				t = []
				t.append(thumbnail.url)
			a.append("<a href='"+entry.media.player.url+"'><img src="+t[0]+" alt="+entry.media.title.text+" title="+entry.media.title.text+" /></a>")
	datafeed = "http://gdata.youtube.com/feeds/api/videos?q=tricking&orderby=published&category=tricking&max-results=30"
	GetAndPrintVideoFeed(datafeed)
	t = get_template('base.html')
	html = t.render(Context({'content': a}))
	return HttpResponse(html)
