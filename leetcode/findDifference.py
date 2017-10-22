def findDifference(s,t):
	s = list(s)
	for i in t:
		if(i not in s):
			return i
	return None

print(findDifference("abcd","abcde"))


