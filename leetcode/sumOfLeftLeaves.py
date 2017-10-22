def sumOfLeftLeaves(root):
	if not root:
		return 0
	if root.left and not root.left.left and not root.left.right:
		return root.left.data + sumOfLeftLeaves(root.right)
	return sumOfLeftLeaves(root.left)+sumOfLeftLeaves(root.right)
