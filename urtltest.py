import urllib2
import json

url = "http://gdata.youtube.com/feeds/api/videos?q=tricking&alt=json&format=5&orderby=published&category=tricking&max-results=30"
response = urllib2.urlopen(url)
v_data = json.load(response)
data = json.dumps(v_data['feed']['entry'] , sort_keys=True, indent=4, separators=(',',': '))

print data
