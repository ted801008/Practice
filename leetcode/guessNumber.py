def guessNumber(n):
	l = 1
	h = n
	while(l<h):
		mid = (1+n)/2
		if(guess(mid)==-1):
			h = mid-1
		if(guess(mid==1)):
			l = mid+1
		if(guess(mid==0)):
			print(mid) 
			break