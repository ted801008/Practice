def numberComplement(x):
	i = 1
	while(i<=x):
		i = i<<1
	return (i-1)^x

print(numberComplement(1))

