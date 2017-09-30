class Node:
	def __init__(self,fro,to):
		self.fro = fro
		self.to = to

class edgelist:
	def __init__(self,N):
		self.elist = []
		self.N = N
		self.idx = 0
		for i in range(N):
			self.elist.append([])
			

	def add(self,fro,to):
		self.elist[fro].insert(0,Node(fro,to))
		self.idx+=1

	def display(self):
		for i in range(self.N):
			for j in range(len(self.elist[i])):
				print(self.elist[i][j].fro,self.elist[i][j].to)

m1 = [[0,1,1,0],[1,0,0,0],[0,0,0,1],[1,0,0,0]]
e1 = edgelist(len(m1))
for i in range(len(m1)):
	for j in range(len(m1[i])):
		if (i!=j and m1[i][j]!=0):
			e1.add(i,j)
e1.display()