def reverseInteger(x):
	newX = [i for i in str(x) if i != "-"][::-1]
	newX = int("".join(newX))
	if(x<0):
		return (-1)*newX
	else:
		return newX

print(reverseInteger(-123))

