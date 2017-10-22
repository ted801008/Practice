def nextGreaterElement(x,y):
	result = [-1]*len(x)
	for i in range(len(x)):
		for j in range(y.index(x[i])+1,len(y)):
			if(x[i]<y[j]):
				result[i] = y[j]
				break
	return result

print(nextGreaterElement([2,4],[1,2,3,4]))
