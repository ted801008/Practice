def minIndexSumOfTwoList(x,y):
	xIndex = {i:j for i,j in enumerate(x)}
	best,ans = 1e9,[]
	bestans = 0
	for i,j in enumerate(y):
		if(j in xIndex.values()):
			ans.append(j)
			if (best>(x.index(j)+i)):
				best = x.index(j)+i
				bestans = j
			
	return [bestans]

print(minIndexSumOfTwoList(["Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Shogun", "Burger King"]))
