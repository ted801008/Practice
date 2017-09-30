def removeDuplicatesFromSortedArray(x):
	length = len(x)-1
	count = 0
	while length>=0:
		if (x[length]==x[length-1]):
			length-=1
		else:
			count+=1
			length-=1
	return count

print(removeDuplicatesFromSortedArray([1,1,2,2,3,4,4]))
