#condision practice

score = input("Enter Score: ")

try:
	score = float(score)
except:
	print("Not a number")
	
if score > 1:
  print("too high")
elif score < 0:
  print("too low")
elif score >= 0.9:
	print("A")
elif score >= 0.8:
  print("B")
elif score >= 0.7:
  print("C")
elif score >= 0.6:
  print("D")
elif score < 0.6:
  print("F")