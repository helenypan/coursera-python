name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hr_dict = dict()
for line in handle:
	if line.startswith("From "):
		line_words = line.split()
		time = line_words[5]
		hr= time.split(":")[0]
		hr_dict[hr] = hr_dict.get(hr, 0) + 1

hr_list = list()
for hr, count in hr_dict.items():
	hr_list.append((hr, count))
hr_list.sort()
print hr_list
for hr,count in hr_list:
	print hr, count
