def relativeRanks(data):
	data = sorted(data)
	rank = ["Gold Medal","Silver Medal","Bronze Medal"]+data[3:len(data)]
	print(rank)

relativeRanks([5,4,3,2,1])
