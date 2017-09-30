def isPalindrome(x):
	length = len(str(x)) 
	len1 = (length//2)-1 
	if length%2==0:
		return False
	res = 0
	while len1>=0:
		res+=((x%10)*(10**(len1)))
		x = x//10  
		len1-=1
	x = x//10
	if (x==res):
		return True
	else:
		return False



print(isPalindrome(11011))
