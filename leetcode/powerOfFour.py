import math
def powerOfFlour(n):
	x = math.log(n,4)
	return (round(x,0)==x)

print(powerOfFlour(64))
