class MyQueue(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.queue = []

	def push(self,x):
		self.queue.append(x)
		if(self.head == None):
			self.head=self.tail= x
		else:
			self.tail = x
	def pop(self):
		if(self.head==self.tail):
			if(self.head==None):
				return None
			else:
				x = self.head
				self.queue.remove(x)
				self.head=self.tail = None
				return x
		else:
			x = self.head
			self.head = self.queue[1]
			self.queue.remove(self.head)
			return x

	def peek(self):
		return self.tail

	def empty(self):
		if(self.head==self.tail==None):
			return True
		return False

	def print(self):
		for i in self.queue:
			print(i)

q1 = MyQueue()
q1.push(1)
print(q1.pop())
print(q1.empty())