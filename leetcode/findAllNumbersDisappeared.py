def findAllNumbersDisappearedInAnArray(nums):
	for i in range(1,len(nums)+1):
		if i not in nums:
			print(i)

findAllNumbersDisappearedInAnArray([4,3,2,7,8,2,3,1])