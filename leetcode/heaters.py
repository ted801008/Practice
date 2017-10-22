def findRadius(houses,heaters):
	notEncluded = [heaters[0]-1]
	for i in range(1,len(heaters)):
		notEncluded.append(heaters[i]-heaters[i-1]-1)
	if(max(notEncluded)==1):
		return 1
	else:
		return (round(max(notEncluded)//2))

print(findRadius([1,2,3],[2]))