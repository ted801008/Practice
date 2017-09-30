class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class arrlist:
	def __init__(self,N):
		self.arr = []
		self.N = N
		for i in range(N):
			self.arr.append(Node(i))

	def add(self,fro,to):
		newnode = Node(to)
		temp = self.arr[fro].next
		self.arr[fro].next = newnode
		newnode.next = temp

	def display(self):
		for i in range(self.N):
			p = self.arr[i].next
			while(p!=None):
				print(i,p.data)
				p = p.next

m1 = [[0,1,1,0],[1,0,0,0],[0,0,0,1],[1,0,0,0]]
a1 = arrlist(len(m1))
for i in range(len(m1)):
	for j in range(len(m1[i])):
		if(m1[i][j]==1 and i!=j):
			a1.add(i,j)
a1.display()