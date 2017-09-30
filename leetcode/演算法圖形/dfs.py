class dfs:
	def __init__(self,m):
		self.N = len(m)
		self.visted = []
		for i in range(self.N):
			self.visted.append(False)
		self.adjlist = m

	def search(self,n):
		print(n)
		self.visted[n]=True
		for i in range(self.N):
			if(self.adjlist[n][i]==1 and self.visted[i]==False):
				self.search(i)


m1 = [[0,1,0,0,1],[1,0,1,1,0],[0,1,0,0,0],[0,1,0,0,0],[1,0,0,0,0]]
d1 = dfs(m1)
d1.search(0)  