def reverseStringII(str,k):
	str = list(str)
	for i in range(0,len(str),2*k):
		str[i:i+k] = reversed(str[i:i+k])
	return "".join(str)

print(reverseStringII("abcdefg",3))