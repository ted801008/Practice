def reshapeMatrix(data,r,c):
	if(len(data)*len(data[0])!=r*c):
		return data
	i = 0
	vals = [val for row in data for val in row]
	step = len(vals)//r
	result = []
	while(i<len(vals)):
		result.append(vals[i:i+step])
		i+=step
	return result

print(reshapeMatrix([[1,2],[3,4]],2,4))

