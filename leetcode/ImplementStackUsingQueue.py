class MyStack(object):
	def __init__(self):
		self.stack = []
		self.head = None

	def push(self,x):
		if(self.head==None):
			self.head = x
		self.stack.append(x)

	def pop(self):
		data = self.stack[-1]
		self.stack.remove(data)
		return data

	def top(self):
		return self.stack[-1]

	def empty(self):
		if(self.head==None):
			return True
		return False

