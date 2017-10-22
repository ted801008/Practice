def countBits(num):
	countlist = [0]
	for i in range(1,num+1):
		count = 1
		while(i//2!=0):
			res = i%2
			i = i/2
			if(res==1):
				count+=1
		countlist.append(count)
	return countlist

def countBits1(num):
	iniArr = [0]
	if num>0:
		amountToAdd = 1
		while(len(iniArr)<num+1):
			iniArr.extend([x+1 for x in iniArr])
			print(iniArr)
	return iniArr[0:num+1]

print(countBits1(5))
