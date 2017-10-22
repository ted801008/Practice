class Solution(object):
	def __init__(self,nums):
		self.nums = nums
	def majorityElement(self):
		while(max(self.nums)!=min(self.nums)):
			self.divide()
		print(max(self.nums))
	def divide(self):
		length = round(len(self.nums)/2+0.1)
		for i in range(length-1):
			print(i,i+length)
			if self.nums[i] not in self.nums[length:]:
				self.nums = [x for x in self.nums if x !=self.nums[i]]
			if self.nums[i+length-1] not in self.nums[:length]:
				self.nums = [x for x in self.nums if x !=self.nums[i+length-1]]


s1 = Solution([2,2,2,2,2,4,4])
s1.majorityElement()

	


