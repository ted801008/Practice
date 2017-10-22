def moveZeroes(x):
	for i in x:
		if i==0:
			x.remove(i)
			x.append(0)
	return x

print(moveZeroes([0,1,0,3,12]))

