def implementstrStr(haystack,needle):
	for i in range(len(haystack)-len(needle)+1):
		if(haystack[i:i+len(needle)]==needle):
			return i
	return -1

haystack = "kobebryant"
needle = "be"
print(implementstrStr(haystack,needle))