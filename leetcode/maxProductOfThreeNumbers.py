class Solution(object):
	def __init__(self,nums):
		self.nums = nums
	def maxProductOfThreeNumbers(self):
		first = self.getMax()
		second = self.getMax()
		third = self.getMax()
		return first*second*third
	def getMax(self):
		maxValue = max(self.nums)
		self.nums.remove(maxValue)
		return maxValue

s1 = Solution([1,2,3])
print(s1.maxProductOfThreeNumbers())