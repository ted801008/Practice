import numpy as np
class prim:
	def __init__(self,m1):
		self.N = len(m1)
		self.Aset = np.ones((self.N))
		self.Bset = np.zeros((self.N))
		self.T = np.ones((self.N,self.N))*100
		self.m1 = m1

	def search(self,n):
		while True:
			if(np.all(self.Aset==0)==True):
				break
			print(n)
			self.Aset[n] = 0
			self.Bset[n] = 1
			mini = 100000
			ti = 0
			tj = 0
			for i in range(self.N):
				for j in range(self.N):
					if(self.Aset[j]==1 and self.Bset[i]==1):
						self.T[i][j] = m1[i][j]
			for k in range(self.N):
				for k2 in range(self.N):
					if(mini>self.T[k][k2] and self.Bset[k2]!=1):
						mini = self.T[k][k2]
						ti = k
						tj = k2

			self.T[ti][tj] = 100
			self.search(tj)


			
m1 = [[100,4,6,100,3,100],[4,100,5,2,100,100],[6,5,100,100,7,8],[100,2,100,100,100,100],[3,100,7,100,100,100],[100,100,8,100,100,100]]
p1 = prim(m1)
p1.search(0)