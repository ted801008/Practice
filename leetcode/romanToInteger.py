romanList = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
def romantointeger(x):
	roman = [i for i in x]
	length = len(roman)-1
	Sum = 0
	while length>=0:
		if(length-1>=0):
			if(romanList[roman[length]]>romanList[roman[length-1]]):
				Sum += (romanList[roman[length]]-romanList[roman[length-1]])
			else:
				Sum += (romanList[roman[length]]+romanList[roman[length-1]])
			length-=2
		else:
			Sum+=romanList[roman[length]]
			length-=1
	return Sum
print(romantointeger("MCMLXX"))