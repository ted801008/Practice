def secondMinNodeInBinaryTree(t1):
	ans = float('inf')
	min = t1.root.data

	def dfs(node):
		if min<node.data<ans:
			ans = node
		elif node.data==min:
			dfs(node.left)
			dfs(node.right)
	dfs(root)
	return ans if ans<float('inf') else -1