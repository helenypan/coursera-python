import sqlite3

conn = sqlite3.connect("db_email.sqlite")
cur = conn.cursor()

cur.execute('''
	DROP TABLE IF EXISTS Counts''')

cur.execute('''
	CREATE TABLE Counts(email TEXT, count INTEGER)''')

fname = raw_input("Enter file name:")
if(len(fname)<1) :
	fname = "mbox-short.txt"
fh = open(fname)
for line in fh:
	if not line.startswith("From: "):
		continue
	pieces = line.split()
	email = pieces[1]
	cur.execute('SELECT count FROM Counts where email=?', (email,))
	try:
		count = cur.fetchone()[0]
		cur.execute('UPDATE Counts SET count = count 1 WHERE email=?',(email, ))
	except:
		cur.execute('''
			INSERT INTO Counts(email, count) VALUES(?,1)''',(email, ))
	conn.commit() # very important

sqlstr = "SELECT email, count FROM Counts ORDER BY count DESC Limit 10"

for row in cur.execute(sqlstr):
	print (row[0],row[1])

cur.close()