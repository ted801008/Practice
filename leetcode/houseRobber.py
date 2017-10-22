def rob(nums):
	last, now = 0, 0
	for i in nums:
		last,now = now,max(last+i,now)

	return now

print(rob([12,3,1,16]))
