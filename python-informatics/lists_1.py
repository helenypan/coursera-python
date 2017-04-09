# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) == 0:
	fname = "romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    line_list  = line.split()
    for word in line_list:
    	if word not in lst:
    		lst.append(word)
lst.sort()
print lst