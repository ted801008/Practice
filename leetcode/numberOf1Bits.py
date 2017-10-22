import math
def numberOf1Bits(x):
	z = 1
	x = int(x,2)
	while(z<x):
		z*=2
	z = int(z//2)
	return x-z

	



print(numberOf1Bits(bin(11)))