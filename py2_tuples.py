#practice tuples

name = input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d = dict()
for line in handle:
	if line.startswith("From:") or not line.startswith("From") : continue
	words = line.split()
	times = words[5].split(":")
	d[times[0]] = d.get(times[0], 0) + 1

for h, count in sorted(d.items()):
	print(h, count)