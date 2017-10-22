def islandPerimeter(grid):
	count = 0
	count1 = 0
	for i in range(len(grid)):
		for j in range(len(grid)):
			if(grid[i][j]==1):
				count1+=1
				if(0<=i-1<len(grid) and grid[i-1][j]):
					count+=1
				if(0<=i+1<len(grid) and grid[i+1][j]):
					count+=1
	return (4*count1)-count-(count1-1)

print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))

