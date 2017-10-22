def poorPigs(buckets,minutesToDie,minutesToTest):
	pigs = 0
	while(minutesToTest/minutesToDie)**pigs<buckets:
		pigs+=1
	return pigs