def searchInsertPosition(data,k):
	result = 0
	if(k>data[-1]):
		return (len(data))
	for i,j in enumerate(data):
		if(j>=k):
			result = i
			break
	return (result)

print(searchInsertPosition([1,3,5,6],0))