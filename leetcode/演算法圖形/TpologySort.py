class ANode:
	def __init__(self,data):
		self.data = data
		self.next = None
class AList:
	def __init__(self,indegree):
		self.indegree = indegree
		self.head = None
class TpologySort:
	def __init__(self,m1):
		self.N = len(m1)
		self.top = -1
		self.adjlist = []
		for i in range(self.N):
			degree = 0
			for j in range(self.N):
				degree+=m1[j][i]
			if(degree==0):
				degree = self.top
				self.top = i
			self.adjlist.insert(i,AList(degree))
			for j in range(self.N):
				if(m1[i][j]!=0):
					node = ANode(j)
					node.next = self.adjlist[i].head
					self.adjlist[i].head = node
	def sort(self):
		while(self.top!=-1):
			j = self.top
			print(j)
			self.top = self.adjlist[j].indegree
			p = self.adjlist[j].head
			while(p!=None):
				k = p.data
				self.adjlist[k].indegree-=1
				if(self.adjlist[k].indegree==0):
					self.adjlist[k].indegree = self.top
					self.top = k
				p=p.next





data = [[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,1,1],[0,0,0,0,1,1,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
t1 = TpologySort(data)
t1.sort()



