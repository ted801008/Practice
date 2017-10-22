def findMaxConsecutiveOnes(nums):
	nums = nums+[0]
	max = -float("inf")
	prev = 1
	distance = 0
	for i in range(len(nums)):
		if(nums[i]==0):
			distance = i-prev-1
			prev = i
		if(max<distance):
			max = distance
	return max
nums = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))