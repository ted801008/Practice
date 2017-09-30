def judgeRouteCircle(Order):
	UD = 0
	RL = 0
	for i in Order:
		if(i=="U" or i=="D"):
			UD+=1
		else:
			RL+=1
	if(UD%2==0 and RL%2==0):
		return True
	return False

print(judgeRouteCircle("RL"))
