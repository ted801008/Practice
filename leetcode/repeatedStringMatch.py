def repeatedStringMatch(A,B):
	i = 1
	while (B not in A):
		i+=1
		A = A*2
	return i

print(repeatedStringMatch("abcd","cdabcdab"))