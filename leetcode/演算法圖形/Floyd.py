class Floyd:
	def __init__(self,m1):
		self.N = len(m1)
		self.m1 = m1

	def travel(self):
		
		for k in range(self.N):
			for i in range(self.N):
				for j in range(self.N):
					if(self.m1[i][j]>self.m1[i][k]+self.m1[k][j]):
						self.m1[i][j] = self.m1[i][k]+self.m1[k][j]

		return self.m1
data = [[0,1,6,100,8,100],
		[1,0,3,5,100,100],
		[6,3,0,5,4,10],
		[100,5,5,0,100,5],
		[8,100,4,100,0,100],
		[100,100,10,5,100,0]]
f1 = Floyd(data)
print(f1.travel())