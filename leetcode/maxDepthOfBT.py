class TreeNode(object):
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None
class Tree(object):
	def __init__(self):
		self.root = None
	def add(self,data):
		if(self.root == None):
			self.root = TreeNode(data)
		else:
			self._add(self.root,data)
	def _add(self,root,data):
		if(data<root.data):
			if(root.left!=None):
				self._add(root.left,data)
			else:
				root.left = TreeNode(data)
		else:
			if(root.right!=None):
				self._add(root.right,data)
			else:
				root.right = TreeNode(data)

class Solution(object):
	def __init__(self):
		self.depth = -1
	def maxDepth(self,root):
		if root == None:
			return 0
		else:
			count = 1
			return self._maxDepth(root,count)
	def _maxDepth(self,root,count):
		if(not root.left and not root.right):
			if(self.depth<count):
				self.depth = count
		elif root.left:
			count+=1
			self._maxDepth(root.left,count)
		elif root.right:
			count+=1
			self._maxDepth(root.right,count)

t1 = Tree()
t1.add(2)
t1.add(4)
t1.add(1)
t1.add(3)
t1.add(0)
t1.add(8)
s1 = Solution()
s1.maxDepth(t1.root)
print(s1.depth)
