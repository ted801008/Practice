import math
def primeNumber(N):
	for i in range(2,N):
		flag = 1
		k = int(i**0.5)
		for j in range(2,k+1):
			if(i%j==0):
				flag = 0
				break
		if(flag):
			print(i)

primeNumber(10)




