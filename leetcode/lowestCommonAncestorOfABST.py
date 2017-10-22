class TreeNode(object):
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None
class Tree(object):
	def __init__(self):
		self.root = None
	def add(self,data):
		if(self.root==None):
			self.root = TreeNode(data)
		else:
			self._add(self.root,data)
	def _add(self,root,data):
		if(root.data<data):
			if(root.right):
				self._add(root.right,data)
			else:
				root.right = TreeNode(data)
		else:
			if(root.left):
				self._add(root.left,data)
			else:
				root.left = TreeNode(data)
class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
	    while root:
	        if root.data > p.data and root.data > q.data:
	            root = root.left
	        elif root.data < p.data and root.data < q.data:
	            root = root.right
	        else:
	            return root.data

t1 = Tree()
t1.add(6)
t1.add(2)
t1.add(8)
t1.add(0)
t1.add(4)
t1.add(3)
t1.add(5)
t1.add(8)
t1.add(7)
t1.add(9)
s1 = Solution()
p = t1.root.left
q = t1.root.right
print(s1.lowestCommonAncestor(t1.root,p,q))
