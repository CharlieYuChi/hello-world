#practice dictionary

name = input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()

for line in handle:
	if not line.startswith("From:") : continue
	words = line.split()
	d[words[1]] = d.get(words[1],0) + 1

bigname = None
bignum = None

for word, count in d.items():
	if bigname is None or count > bignum:
		bigname = word
		bignum = count
print(bigname, bignum)
