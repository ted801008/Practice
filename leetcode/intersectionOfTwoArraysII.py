import collections
def intersect(nums1,nums2):
	a = collections.Counter(nums1)
	b = collections.Counter(nums2)
	print(a)
	print(b)
	print(list(a&b))

intersect([1,2,2,1],[2,1])