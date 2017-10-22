def reverseVowel(str):
	vowel = ['a','e','i','o','u','A','E','I','O','U']
	past = 0
	current = 0
	str = list(str)
	for i,j in enumerate(str):
		if(j in vowel):
			if(past==0):
				past=current=i
				continue
			else:
				current = i
		str[current],str[past] = str[past],str[current]
		past = current
	return ''.join(str)

print(reverseVowel("leetcode"))