def happyNumber(nums):
	sum = 0
	while(sum!=1):
		sum = 0
		for i in str(nums):
			sum+=(int(i)**2)	
		nums = sum
	return True
print(happyNumber(20))
