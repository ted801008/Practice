def maxSubarray(nums):
	maxSum = 0
	for i in range(len(nums)):
		temMaxSum = 0
		for j in range(i,len(nums)):
			temMaxSum+=nums[j]
			if(maxSum<temMaxSum):
				maxSum = temMaxSum
	return maxSum

print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))