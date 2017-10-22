def nonDecreasingArray(x):
	count = 0
	for i in range(len(x)-1):
		if(x[i]>x[i+1]):
			count+=1
	if(count>1):
		return False
	else:
		return True

print(nonDecreasingArray([4,2,3]))