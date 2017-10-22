import math
def powerOfThree(n):
	x = math.log(n,3)
	return (x==round(x,0))

print(powerOfThree(81))	