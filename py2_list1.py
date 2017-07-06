#practice list1

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
things = list()
for line in fh:
	things = line.split()
	for thing in things:
		if thing not in lst:
			lst.append(thing)
lst.sort()
print(lst)