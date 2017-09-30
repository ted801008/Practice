def ArrayPartition(x):
	x = sorted(x)
	sum = 0
	i = 0
	while(i<len(x)):
		sum+=x[i]
		if(len(x)==(i+2)):
			sum+=x[i+1]
			break

		i+=2
		
	return sum

x = [1,4,3,2,2]
print(ArrayPartition(x))
