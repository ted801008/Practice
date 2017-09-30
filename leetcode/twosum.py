def twosum(target,nums):
	newnums = [x for x in nums if x<target]
	for i in range(len(newnums)):
		index = i
		while i<len(newnums):
			sum = newnums[index]+newnums[i]
			if(target==sum):
				return [index,i]
			i+=1
	return None

