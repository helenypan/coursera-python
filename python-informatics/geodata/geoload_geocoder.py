import geocoder
import sqlite3

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

fh = open("where.data")
count = 0
for line in fh:
    address = line.strip()
    cur.execute("SELECT * FROM Coordinates WHERE address= ?", (buffer(address), ))

    try:
        data = cur.fetchone()[0]
        print "Found in database ",address
        continue
    except:
        pass

    print 'Resolving', address
    g = geocoder.google(address)
    latlng = g.latlng
    try:
        (latitude, longitude) = latlng
        print address, latitude,longitude
        cur.execute('''INSERT INTO Coordinates (address, latitude, longitude) 
            VALUES ( ?, ? ,?)''', ( buffer(address),latitude,longitude ) )
        conn.commit() 
    except:
        print address, "Failed to retrieve lat lng", latlng


print "Run geodump.py to read the data from the database so you can visualize it on a map."
