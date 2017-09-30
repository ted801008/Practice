def distributeCandies(x):
	category = len(set(x))
	half = len(x)//2
	if(category>half):
		return half
	else:
		return category

candies = [1,1,2,3]
print(distributeCandies(candies))
