class Solution(object):
	def maxCount(self,m,n,ops):
		data = [[0]*m]*n
		length = len(ops)
		row = 100
		column = 100
		for i in ops:
			if row>i[0]:
				row = i[0]
			if column>i[1]:
				column = i[1]
		return (length,row*column)

s1 = Solution()
print(s1.maxCount(3,3,[[2,2],[3,3]]))

