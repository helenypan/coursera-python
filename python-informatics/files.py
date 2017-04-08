# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    colon_pos = line.rstrip().find(":")
    num = float(line[colon_pos+1:])
    total = total + num
    count = count + 1 
print "Average spam confidence:", float(total)/float(count)