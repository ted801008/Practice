def missingNumber(x):
	for i in range(len(x)):
		if(x[i+1]-x[i]!=1):
			return int((x[i+1]+x[i])/2)
print(missingNumber([0,1,2,4,5,6]))