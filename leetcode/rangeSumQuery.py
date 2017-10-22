class NumArray(object):
	def __init__(self,nums):
		self.nums = nums

	def sumRange(self,i,j):
		return sum(self.nums[i:j+1])

n1 = NumArray([-2,0,3,-5,2,-1])
print(n1.sumRange(2,5))