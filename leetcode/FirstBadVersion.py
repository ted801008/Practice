def firstBadVersion(ori,n):
	if(ori==n):
		return n
	half = round((n+ori)/2+0.1)
	judge = isBadVersion(half)
	if(judge==False):
		firstBadVersion(half-1,n)
	else:
		firstBadVersion(ori,half+1)
