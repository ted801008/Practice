def mergeTwoSorted(a,b):
	result = []
	i = len(a)-1 #3
	j = len(b)-1 #3

	while (i>=0 and j>=0):
		if(a[i]<b[j]):
			result.append(b.pop())
			j-=1
		elif(a[i]>=b[j]):
			result.append(a.pop())
			i-=1
		else:
			if a==[]:
				result.append(b.pop())
				j-=1
			else:
				result.append(a.pop())
				i-=1
	return sorted(result)
print(mergeTwoSorted([1,3,6,7],[2,6,8,10]))