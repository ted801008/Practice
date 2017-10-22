def isMatch(s,t):
	if not (s and t):
		return s is t
	return (s.data==t.data and isMatch(s.left,t.left) and isMatch(s.right,t.right))

def isSubtree(s,t):
	if (isMatch(s,t)):
		return True
	if not s:
		return False
	return isSubtree(s.left,t) or isSubtree(s.right,t)