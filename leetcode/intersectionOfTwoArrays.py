def intersection(nums1,nums2):
	ans = []
	if(len(nums1)>len(nums2)):
		for i in nums2:
			if(i in nums1 and i not in ans):
				ans.append(i)
	else:
		for i in nums1:
			if(i in nums2 and i not in ans):
				ans.append(i)

	return ans

print(intersection([1,2,2,1],[2,2]))