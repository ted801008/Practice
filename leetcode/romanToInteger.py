def romanToInteger(str):
	roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
	z = 0
	for i in range(0,len(str)-1):
		if(roman[str[i]]<roman[str[i+1]]):
			z-=roman[str[i]]
		else:
			z+=roman[str[i]]
	return z+roman[str[-1]]

x = "III"
print(romanToInteger(x))