def singleNumber(data):
	return 2*sum(set(data))-sum(data)

print(singleNumber([2,2,3,4,3]))