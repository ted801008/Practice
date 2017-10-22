def pascalsTriangleII(k):
	row = [1]
	for i in range(k):
		row = [x+y for x,y in zip([0]+row,row+[0])]
	return row
print(pascalsTriangleII(5))
