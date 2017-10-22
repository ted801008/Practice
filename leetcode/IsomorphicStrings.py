def isIsomorphic(s,t):
	mapDict = dict()
	s = list(s)
	t = list(t)
	for i in range(len(s)):
		if(s[i] in mapDict.keys()):
			if(t[i] != mapDict[s[i]]):
				return False
		mapDict[s[i]]=t[i]
	return True

print(isIsomorphic("paper","title"))