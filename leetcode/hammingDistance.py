def hammingDistance(x,y):
	return bin(x^y).count('1')


print(hammingDistance(4,1))
