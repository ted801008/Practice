import numpy as np
class dijkstra:
	def __init__(self,m1):
		self.N = len(m1)
		self.m1 = m1
		self.distance = m1[0]
		self.visted = [0]*self.N
		self.visted[0] = 1

	def travel(self):
		for k in range(5):	
			for i in range(self.N):
				for j in range(self.N):
					if(self.visted[j]==1 and i is not j ):
						if self.distance[j]+self.m1[j][i]<self.distance[i]:
							self.distance[i] = self.distance[j]+self.m1[j][i]

			
			mini = 100000
			nindex = 0
			for i in range(self.N):
				if self.visted[i]==0:
					if(mini>self.distance[i]):
						mini = self.distance[i]
						nindex = i
			self.visted[nindex] = 1

		return self.distance

data = [[0,1,4,100,8,100],
		[1,0,3,5,100,100],
		[4,3,0,5,4,10],
		[100,5,5,0,100,5],
		[8,100,4,100,0,100],
		[100,100,10,5,100,0]]
d1 = dijkstra(data)
print(d1.travel())

