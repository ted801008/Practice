def perfectNumber(num):
	top = num//2
	ans = 0
	for i in range(1,top+1):
		if(num%i==0):
			ans+=i
	if(ans==num):
		return True
	else:
		return False

print(perfectNumber(27))
