class Solution(object):
	def constructMaxBT(self,nums):
		dummy = TreeNode(None)
		def q(root,nums):
			if not nums:
				return
			maxindex = nums.index(max(nums))
			root.data = nums[maxindex]
			if nums[:maxindex]:
				root.left = TreeNode(None)
				q(root.left,nums[:maxindex])
			if nums[maxindex+1:]:
				root.right = TreeNode(None)
				q(root.right,nums[maxindex+1:])
		q(dummy,nums)
		return dummy

