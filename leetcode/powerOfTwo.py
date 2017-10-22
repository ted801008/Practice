import math
def powerOfTwo(n):
	if(n == 2 ** int(math.sqrt(n)) or n == 2**int(math.sqrt(n)+1)):
		return True
	else:
		return False


print(powerOfTwo(8))
