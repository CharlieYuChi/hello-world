#practice function

def computepay(h,r):
	t = 0
	if h > 40:
		t = h - 40
		h = 40
	return h * r + t * r * 1.5

hrs = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))
p = computepay(hrs, rate)
print(p)