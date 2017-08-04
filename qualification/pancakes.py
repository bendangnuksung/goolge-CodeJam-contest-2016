times=int(input())
string = []
for x in range(times):
	string.append(input())
for i in range(len(string)):
	count=0
	for x in range(1,len(string[i])):
		if string[i][x:x+1] != string[i][x-1:x]:
			count +=1
	if string[i][-1:] == '-':
		count +=1
	print ("#case",i+1, ": ",count)
