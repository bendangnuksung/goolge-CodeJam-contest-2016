import math

def prime(data):
	for i in range (2,data):
		if data%i==0:
			return 1, i
	return 0,0

times= int(input())
while(times):
	N= int(input())
	J= int(input())
	# saving all the combination of the input eg: N=3, saving to data= 101,111
	data=[]
	length = N-2
	size_string = math.pow(2,length)
	for x in range(int(size_string)):
		temp= bin(x)[2:]
		data.append('1' + '0'*(length- len(temp))+ temp + '1')
	counter=0

	print("#case ", (times+1)-times,":")
	#iterating each data, checking each data is a prime from base: 2-10
	for x in data:
		flag=1
		divisor=[]
		for y in range(2,11):
			s=int(x,y)
			p,q= prime(s)
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

	##output will be slight different as shown in website, but it fulfills all condition. 
	##output N=16 and J=50 takes a lot of time










