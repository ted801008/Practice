def maxAverageSubarray(nums,k):
	best = -float("inf")
	for i in range(len(nums)-4):
		Allsum = sum(nums[i:i+k])

		if(best<Allsum):
			best = Allsum
	return best/k

nums = [1,12,-5,-6,50,3]
print(maxAverageSubarray(nums,4))
