def findAnagrams(s,p):
	p = sorted(list(p))
	judge = [False]*len(s)
	for i in range(len(s)):
		if s[i] in p:
			judge[i]=True
	newList = [i for i in range(len(s)) if judge[i:i+3]==[True,True,True]]
	for i in newList:
		if(sorted(s[i:i+3])==p):
			print(i)

(findAnagrams("cbaebabacd","abc"))

