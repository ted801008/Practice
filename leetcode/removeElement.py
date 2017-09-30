def removeElement(nums,val):
	start,end = 0,len(nums)-1
	while(start<=end):
		if(nums[start]==val):
			nums[start] = nums[end]
			end-=1
		else:
			start+=1
	return start

nums = [3,2,2,3]
print(removeElement(nums,3))