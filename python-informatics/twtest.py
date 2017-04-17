import urllib
import twurl

print '* Calling Twitter...'
url = twurl.augment("https://api.twitter.com/1.1/statuses/user_timeline.json",
	{'screen_name':'drchuck', 'count': '2'})
# print url
connection = urllib.urlopen(url)
data = connection.read()
# print data
headers = connection.info()
print "original headers", type(headers)
print headers
headers_dict = headers.dict
print "original headers converted to dict:"
print headers_dict