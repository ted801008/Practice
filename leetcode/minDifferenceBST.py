class TreeNode(object):
	def __init__(self,x):
		self.val = x
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
		if(val<node.val):
			if(node.left!=None):
				self._add(val,node.left)
			else:
				node.left = TreeNode(val)
		else:
			if(node.right!=None):
				self._add(val,node.right)
			else:
				node.right = TreeNode(val)
	def find(self,val):
		if(self.root!=None):
			return self._find(val,self.root)
		else:
			return None
	def _find(self,val,node):
		if(val==node.val):
			return node
		elif(val<node.val and node.left!=None):
			self._find(val,node.left)
		elif(val>node.val and node.right!=None):
			self._find(val,node.right)
	def printTree(self):
		if(self.root!=None):
			return self._printTree(self.root)
	def _printTree(self,node):
		if(node!=None):
			self._printTree(node.left)
			print(str(node.val)+" ")
			self._printTree(node.right)
class Solution(object):
	def __init__(self):
		self.prev = []
		self.min = float("inf")
	def getMinimumDifference(self,root):
		
		self.bst(root)
		return self.min
	def bst(self,node):
		if node.left:
			self.bst(node.left)
		if node.right:
			self.bst(node.right)
		for i in self.prev:
			if(self.min>abs(i-node.val)):
				self.min = abs(i-node.val)
		self.prev.append(node.val)

tree = Tree()
tree.add(1)
tree.add(3)
tree.add(2)
tree.printTree()
s1 = Solution()
print(s1.getMinimumDifference(tree.getRoot()))



