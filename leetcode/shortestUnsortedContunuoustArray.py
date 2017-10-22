def shortestUnsortedContunoustArray(data):
	boolean_same = [a==b for a,b in zip(data,sorted(data))]
	return 0 if all(boolean_same) else len(data)-boolean_same[::-1].index(False)-boolean_same.index(False)

print(shortestUnsortedContunoustArray([2,6,4,8,10,9,15]))