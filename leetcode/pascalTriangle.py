def pascalTriangle(k):
	result = []
	row = [1]
	result.append(row)
	for i in range(k-1):
		row = [x+y for x,y in zip([0]+row,row+[0])]
		result.append(row)
	return result

print(pascalTriangle(5))