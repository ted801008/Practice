
class bfs:
	def __init__(self,m):
		self.N = len(m)
		self.visited = []
		for i in range(self.N):
			self.visited.append(False)
		self.adjlist = m

	def search(self,n):
		q = []
		print(n)
		self.visited[n]=True
		q.append(n)
		while True:
			k = q.pop(0)
			for i in range(self.N):
				if(self.adjlist[k][i]==1 and self.visited[i] is not True):
					print(i)
					q.append(i)
					self.visited[i]=True
			if(q==[]):
				break



m1 = [[0,1,0,0,1],[1,0,1,1,0],[0,1,0,0,0],[0,1,0,0,0],[1,0,0,0,0]]
b1 = bfs(m1)
b1.search(0)