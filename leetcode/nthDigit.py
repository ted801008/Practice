def findNthDigit(n):
	start = 1
	size = 1
	while(n>size):
		n = n-size
		start = start+1
		size = len(str(start))
		print("n:",n)
		print("start:",start)
		print("size:",size)
		print("-"*8)
	return int(str(start)[n-1])

print(findNthDigit(11))