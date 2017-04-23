import sqlite3
# import codecs
import io

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Coordinates')
# fhand = codecs.open('where.js','w', "utf-8")
fhand = io.open('where_2.js',mode='w', encoding="utf-8")
fhand.write(u"myData = [\n")
count = 0
for row in cur :
    lat = row[1]
    lng = row[2]
    if lat == 0 or lng == 0 : continue
    where = str(row[0])
    where = where.replace("'","")
    try :
        print where, lat, lng
        count = count + 1
        if count > 1 : fhand.write(u",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(unicode(output))
    except:
        continue

fhand.write(u"\n];\n")
cur.close()
fhand.close()
print count, "records written to where.js"
print "Open where.html to view the data in a browser"

