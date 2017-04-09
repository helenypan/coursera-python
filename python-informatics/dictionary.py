fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
email_dict = dict()
for line in fh:
	if line.startswith("From "):
		line_words = line.split()
		cur_email = line_words[1]
		email_dict[cur_email] = email_dict.get(cur_email,0) + 1
		

biggest_count = None
biggest_email = None
for email, count in email_dict.items():
	if biggest_count is None or biggest_count < count:
		biggest_count = count
		biggest_email = email

print biggest_email, biggest_count
