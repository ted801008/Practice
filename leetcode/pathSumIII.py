class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def findPath(self,root,sum):
		if sum<0:
			return 0
		if root:
			return int(root.val==sum)+self.findPath(root.left,sum-root.val)+self.findPath(root.right,sum-root.val)
		return 0
	def pathSum(self,root,sum):
		if root:
			return self.findPath(root,sum)+pathSum(root.left,sum)+pathSum(root.right,sum)
		return 0