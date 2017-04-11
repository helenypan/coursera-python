import re

fname = "regex_sum_368588.txt"
handle = open(fname)
num_list = list()
for line in handle:
	line = line.rstrip()
	nums = re.findall('[1-9][0-9]*',line)
	for num in nums:
		num_list.append(int(num))
print sum(num_list)

