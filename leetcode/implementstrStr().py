def strStr(haystack,needle):
	for i in range(len(haystack)-len(needle)+1):
		if needle==haystack[i:len(needle)+i]:
			return i
	return -1


print(strStr("abcd","ab"))