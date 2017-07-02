#practice file

fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
	print("File does not exist!")
	quit()
for line in fh:
	print(line.upper().rstrip())