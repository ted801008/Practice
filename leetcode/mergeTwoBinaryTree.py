class TreeNode(object):
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None
class Tree(object):
	def __init__(self):
		self.root = None
	def add(self,x):
		if(self.root==None):
			self.root = TreeNode(x)
		else:
			self._add(x,self.root)
	def _add(self,x,root):
		if(x>root.data):
			if(root.right):
				self._add(x,root.right)
			else:
				root.right = TreeNode(x)
		else:
			if(root.left):
				self._add(x,root.left)
			else:
				root.left = TreeNode(x)
	def printall(self):
		if(self.root is None):
			return None
		else:
			self._print(self.root)
	def _print(self,node):
		if node:
			self._print(node.left)
			print(node.data)
			self._print(node.right)
class Solution(object):
	def mergeTrees(self,t1,t2):
		if t1 and t2:
			root = TreeNode(t1.data+t2.data)
			root.left = self.mergeTrees(t1.left,t2.left)
			root.right = self.mergeTrees(t1.right,t2.right)
			return root
		else:
			return t1 or t2

t1 = Tree()
t2 = Tree()
t1.add(1)
t1.add(3)
t1.add(2)
t1.add(5)
t2.add(2)
t2.add(1)
t2.add(3)
t2.add(4)
t2.add(7)



s1 = Solution()
root = (s1.mergeTrees(t1.root,t2.root))
