def minMovesToEqualArrayElements(x):
	count = 0
	while(True):
		position = x.index(max(x))
		if x!=len(x)*[max(x)]:
			count+=1
			for i in range(len(x)):
				if(i!=position):
					x[i]+=1
		else:
			break
	
	return count

print(minMovesToEqualArrayElements([1,2,3]))
