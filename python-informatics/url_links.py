import urllib
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/known_by_Charli.html "
process_counter = 1

while process_counter<=7:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	# Retrieve all of the anchor tags
	tags = soup('a')
	link_counter = 1
	for tag in tags:
		if link_counter == 18:
			url = tag.get('href', None)
			break
		link_counter = link_counter + 1
	print url
	process_counter = process_counter + 1
