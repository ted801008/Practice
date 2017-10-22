def plusOne(n):
	length = len(n)
	carry = 0
	res = 0
	k = 1
	while(length>0):
		length-=1
		carry,res = divmod(n[length]+k+carry,10)
		k = 0
		n[length] = res
	if(carry>0):
		return carry
	else:
		return n[0]

print(plusOne([9,9,8]))




