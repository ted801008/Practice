def removeElement(nums,val):
	length = len(nums)
	for i in nums:
		if(i==val):
			length-=1
	return length

print(removeElement([3,2,2,3],3))