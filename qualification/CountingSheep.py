times= int(input())
for i in range(times):
	N = int(input())
	digits = [0,1,2,3,4,5,6,7,8,9]
	lastNumber = 0
	for x in range(1,200):
		temp = x * N
		if not digits:
			print (lastNumber)
			break
		else:
			for x in map(int, str(temp)):
				if x in digits:
					digits.remove(x)
		lastNumber=temp
	print("#case ", i+1, " :", end='')
	print ("INSOMNIA" if digits else lastNumber)
