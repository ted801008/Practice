def factorialTrailingZeros(n):
	return 0 if n==0 else n/5+factorialTrailingZeros(n/5)

print(int(factorialTrailingZeros(25)))