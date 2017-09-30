import numpy as np
class kruskal:
	def __init__(self,m1):
		self.count = 0
		self.m1 = m1
		self.Bset = np.zeros(len(m1))
		self.runlist = np.zeros((len(m1),len(m1)))

	def search(self):
		k = 0
		while (self.count<len(self.m1)-1): #5
			mini = 1000
			ti = 0
			tj = 0
			judge = False
			
			for i in range(len(self.m1)):
				for j in range(len(self.m1)):
					if(self.m1[i][j]<mini and self.runlist[i][j]!=1): #13 ,04,01, 12
						mini = self.m1[i][j]
						ti = i
						tj = j
			#0,1,2,3,4
			if(self.Bset[ti]==1 or self.Bset[tj]==1):
				self.Bset[ti] = 1
				self.Bset[tj] = 1
				for i in range(len(self.Bset)):
					for j in range(len(self.Bset)):
						if(self.Bset[i]==1 and self.Bset[j]==1):
							self.runlist[i][j] = 1
			else:
				self.Bset[ti] = 1
				self.Bset[tj] = 1
				self.runlist[ti][tj] = 1 #13, 31 -> 04, 40 ->
				self.runlist[tj][ti] = 1

			self.m1[ti][tj] = 1000
			self.m1[tj][ti] = 1000
			print(ti,tj)
			self.count+=1

			

m1 = [[100,4,6,100,3,100],[4,100,5,2,100,100],[6,5,100,100,7,8],[100,2,100,100,100,100],[3,100,7,100,100,100],[100,100,8,100,100,100]]
k1 = kruskal(m1)
k1.search()