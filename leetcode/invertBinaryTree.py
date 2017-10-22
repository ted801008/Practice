class TreeNode(object):
	def __init__(self,x):
		self.data =x
		self.left = None
		self.right = None
class Tree(object):
	def __init__(self):
		self.root = None
	def add(self,x):
		if(self.root == None):
			self.root = TreeNode(x)
		else:
			self._add(self.root,x)
	def _add(self,root,x):
		if(root.data<x):
			if(root.right):
				self._add(root.right,x)
			else:
				root.right = TreeNode(x)
		else:
			if(root.left):
				self._add(root.left,x)
			else:
				root.left = TreeNode(x)
	def printAll(self,root):
		if(root==None):
			return None
		else:
			self.printAll(root.left)
			print(root.data)
			self.printAll(root.right)

class Solution(object):
	def invertTree(self,root):
		if(root):
			root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
			return root

t1 = Tree()
t1.add(4)
t1.add(2)
t1.add(7)
t1.add(1)
t1.add(3)
t1.add(6)
t1.add(9)
s1 = Solution()
s1.invertTree(t1.root)
t1.printAll(t1.root)