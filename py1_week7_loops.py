#practice loops

largest = None
smallest = None
first = True
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
    	num = int(num)
    except:
        print('Invalid input')
        continue
    if first == True:
        largest = num
        smallest = num
        first = False
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)