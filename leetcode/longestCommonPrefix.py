def longestCommonPrefix(string):
	string.sort(key = lambda x:len(x))
	str1 = [x for x in string[0]]
	i = 1
	while i<len(string)-1:
		str2 = []
		for j in range(len(str1)):
			if str1[j]==string[i][j]:
				str2.append(str1[j])
		str1 = str2
		i+=1
	result = "".join(str1)
	return result

print(longestCommonPrefix(["abbcd","abbde","abbee"]))



		