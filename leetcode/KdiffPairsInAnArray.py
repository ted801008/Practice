import collections
def findPairs(nums,k):
	if k>0:
		return len(set(nums)&set(n+k for n in nums))
	elif k==0:
		return sum(v>1 for v in collections.Counter(nums).values())
	else:
		return 0

print(findPairs([3,1,4,1,5],2))