import math

def prime(data, used_divisor):
	for i in range (2,data):
		if (data%i==0) and (i not in used_divisor) :
			return 1, i
	return 0,0

times= int(input())
while(times):
	N= int(input())
	J= int(input())
	data=[]
	length = N-2
	size_string = math.pow(2,length)
	for x in range(int(size_string)):
		temp= bin(x)[2:]
		data.append('1' + '0'*(length- len(temp))+ temp + '1')
	counter=0

	for x in data:
		flag=1
		divisor=[]
		used_divisor=[]
		for y in range(2,11):
			s=int(x,y)
			p,q= prime(s,used_divisor)
			used_divisor.append(q)
			divisor.append(q)
			if not p:
				flag=0
				break
		if flag:
			print(x, end='	')
			for i in divisor: print (i, end=' ')
			print()
			counter +=1
		if counter>=J:
			break
	if counter<J:
		print('Could not reach by:', J-counter)
	times -=1










