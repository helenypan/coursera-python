import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1",
	user="root",passwd="root",db="python_learn")

cur = conn.cursor()

cur.execute('''
	DROP TABLE IF EXISTS Counts''')

cur.execute('''
	CREATE TABLE Counts(email TEXT, count INTEGER)''')

fname = raw_input("Enter file name:")
if(len(fname)<1) :
	fname = "mbox.txt"
fh = open(fname)
for line in fh:
	if not line.startswith("From: "):
		continue
	pieces = line.split()
	email = pieces[1]
	cur.execute('SELECT count FROM Counts where email=%s',(email,))
	try:
		count = cur.fetchone()[0]
		cur.execute('UPDATE Counts SET count = count 1 WHERE email=%s' , (email,))
	except:
		cur.execute('INSERT INTO Counts(email, count) VALUES(%s,1)', (email,))
	conn.commit() # very important

sqlstr = "SELECT email, count FROM Counts ORDER BY count DESC Limit 10"

cur.execute(sqlstr)
for row in cur.fetchall():
	print row[0],row[1]

cur.close()