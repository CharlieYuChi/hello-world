#practice file 2

fname = input("Enter file name: ")

try:
	fh = open(fname)
except:
	print("File does not exist!")
	quit()
total, count = 0,0
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	a = line.find(':')
	f = float(line[a+1:].lstrip())
	count += 1
	total += f
print("Average spam confidence: ", str(total/count))