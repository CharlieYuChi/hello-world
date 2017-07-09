#practice regular expression
import re

name = input("Enter file name: ")
if len(name) < 1 : quit()
handle = open(name)
#sum = 0

"""
for line in handle:
	line = line.rstrip()
	stuff = re.findall('[0-9]+', line)
	for i in range(len(stuff)):
		sum += float(stuff[i])
	
print(sum)	
"""

#in one line
print(sum([float(i) for i in re.findall('[0-9]+', handle.read())]))