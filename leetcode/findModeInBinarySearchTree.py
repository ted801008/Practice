import collections
class TreeNode(object):
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
class Tree(object):
	def __init__(self):
		self.root = None
	def getRoot(self):
		return self.root
	def add(self,data):
		if(self.root == None):
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
	def __init__(self):
		self.Count = collections.defaultdict(list)
	def findMode(self,root):
		if(root == None):
			return None
		else:
			self._findMode(root)
		return max(self.Count.items(),key=lambda x:x[1])[0]

	def _findMode(self,root):
		if(root==None):
			return None
		else:
			if str(root.data) not in self.Count.keys():
				self.Count[str(root.data)] = 1
			else:
				self.Count[str(root.data)]+=1
			self._findMode(root.left)
			self._findMode(root.right)

t1 = Tree()
t1.add(1)
t1.add(2)
t1.add(2)
s1 = Solution()
print(s1.findMode(t1.root))
