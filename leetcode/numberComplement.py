def numberComplement(x):
	all = 0
	for i in range(len(x)-2):
		all = all+2**i
	return all^int(x,2)

print(numberComplement(bin(1)))


