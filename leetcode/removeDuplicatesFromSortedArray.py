def removeDuplicatesFromSortedArray(data):
	length = len(data)
	for i in range(length-1):
		if(data[i]==data[i+1]):
			length-=1
	return length

print(removeDuplicatesFromSortedArray([1,1,2]))

