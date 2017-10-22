def setMismatch(nums):
	answer = []
	for i,j in enumerate(nums):
		if(i+1!=j):
			if(i+1<j):
				answer.append(i+1)
				answer.append(j)
			else:
				answer.append(j)
				answer.append(i+1)
	return answer
print(setMismatch([1,2,2,4]))