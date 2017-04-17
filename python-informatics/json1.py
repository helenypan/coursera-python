import urllib
import json

url = "http://python-data.dr-chuck.net/comments_368594.json"
inputs = urllib.urlopen(url).read()

js = json.loads(inputs)

comments = js['comments']
print 'comments count:', len(comments)
total = 0
for item in comments:
	cur_count = item['count']
	total = total + int(cur_count)
print total
    

