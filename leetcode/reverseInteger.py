
def reverseInteger1(x):
	if (x>2**31):
		return 0
	rlist = []
	judge = False
	for i in str(x):
		if i=="-":
			judge = True
		else:
			rlist.append(i)
	rlist.reverse()
	string = "".join(rlist)
	if judge:
		string = "-"+string
		return string
	else:
		return string

def reverseInteger2(x):	
	judge = False
	if x<0:
		judge = True
		x = x*(-1)
	length = len(str(x))-1
	f = 0
	while length>=0:
		int1 = x%10
		x = x//10
		f += (int1*(10**length))
		length-=1
	if judge:
		f = f*(-1)
	return f

print(reverseInteger2(-132))
