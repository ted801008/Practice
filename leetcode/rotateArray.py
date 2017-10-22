def rotateArray(x,n,k):
	x = x[n-k:]+(x[:n-k])
	return x
print(rotateArray([1,2,3,4,5,6,7],7,3))
	