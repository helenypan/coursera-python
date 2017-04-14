import urllib
import xml.etree.ElementTree as ET

url = "http://python-data.dr-chuck.net/comments_368590.xml"
xml_string = urllib.urlopen(url).read()

comment_obj = ET.fromstring(xml_string)

lst = comment_obj.findall('comments/comment')
print 'comments count:', len(lst)
total = 0
for item in lst:
	cur_count = item.find("count").text
	print 'count:', cur_count
	total = total + int(cur_count)
print total
    

