class TreeNode(object):
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
class Tree(object):
	def __init__(self):
		self.root = None
	def getRoot(self):
		return self.root
	def add(self,val):
		if(self.root==None):
			self.root = TreeNode(val)
		else:
			self._add(val,self.root)
	def _add(self,val,node):
		if(node.val>val):
			if(node.left):
				self._add(val,node.left)
			else:
				node.left = TreeNode(val)
		else:
			if(node.right):
				self._add(val,node.right)
			else:
				node.right = TreeNode(val)
	def printall(self):
		if(self.root==None):
			return None
		else:
			self._print(self.root)
	def _print(self,node):
		if(node is not None):
			self._print(node.left)
			print(node.val)
			self._print(node.right)

class Solution(object):
	def minDepth(self, root):
		if not root:
			return 0
		d,D = sorted(map(self.minDepth,(root.left,root.right)))
		return 1+(d or D)

tree = Tree()
tree.add(3)
tree.add(4)
tree.add(10)
tree.add(2)
tree.add(6)
tree.printall()
s1 = Solution()
print(s1.minDepth(tree.getRoot()))