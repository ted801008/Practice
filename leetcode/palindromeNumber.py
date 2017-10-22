def palindromeNumber(x):
	if str(x)[::-1]==str(x):
		return True
	else:
		return False

def palindromeNumberII(x):
	if x<0:
		return False
	ranger = 1
	while x/ranger>=10:
		ranger*=10
	while x:
		left = round(x/ranger)
		right = x%10
		if (left!=right):
			return False
		x = round((x%ranger)/10)
		ranger/=100
		ranger = round(ranger)
		
	return True
print(palindromeNumberII(121))