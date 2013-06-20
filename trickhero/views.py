from django.http import HttpResponse
import gdata.youtube
import gdata.youtube.service

def trick(request):
	a = ["<ul>"]
	def GetAndPrintVideoFeed(uri):
		yt_service = gdata.youtube.service.YouTubeService()
		feed = yt_service.GetYouTubeVideoFeed(uri)
		for entry in feed.entry:
			for thumbnail in entry.media.thumbnail:
				t = []
				t.append(thumbnail.url)
			a.append("<li><a href='"+entry.media.player.url+"'>"+entry.media.title.text+"</a><br /><img src="+t[0]+" alt="+entry.media.title.text+" title="+entry.media.title.text+" /></li>")
	datafeed = "http://gdata.youtube.com/feeds/api/videos?q=tricking&orderby=published&category=tricking&max-results=30"
	GetAndPrintVideoFeed(datafeed)
	a.append("</ul>")
	return HttpResponse(a)
