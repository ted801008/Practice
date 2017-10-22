def sameTree(p,q):
	if p and q:
		return p.data == q.data and sameTree(p.left,q.left) and sameTree(p.left,q.left)
	return p is q
