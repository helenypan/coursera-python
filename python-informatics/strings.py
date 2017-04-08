data = "From stephen.arguard@uct.ac.za Sat Jan 5 09:14:16 2008"
print data
atpost = data.find("@")
sppos  = data.find(" ",atpost)
host = data[atpost+1 : sppos]
print host