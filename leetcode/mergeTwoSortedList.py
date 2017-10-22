class ListNode(object):
	def __init__(self,x):
		self.data = x
		self.next = None
class LinkedList(object):
	def __init__(self):
		self.head = None
	def add(self,x):
		node = self.head
		if(self.head == None):
			self.head = ListNode(x)
		else:
			while(node.next):
				node = node.next
			node.next = ListNode(x)
	def printlist(self):
		node = self.head
		while(node):
			print(node.data)
			node = node.next
def mergeTwoSortedList(x,y):
	xnode = x.head
	ynode = y.head
	newlist = LinkedList()
	while xnode and ynode:
		if xnode.data>ynode.data:
			newlist.add(ynode.data)
			ynode = ynode.next
		else:
			newlist.add(xnode.data)
			xnode = xnode.next
	if xnode:
		while(xnode):
			newlist.add(xnode.data)
			xnode = xnode.next
	else:
		while(ynode):
			newlist.add(xnode.data)
			ynode = ynode.next
	return newlist

l1 = LinkedList()
l1.add(2)
l1.add(5)
l1.add(7)
l2 = LinkedList()
l2.add(1)
l2.add(4)
l2.add(6)
l1.printlist()
print("*"*10)
l2.printlist()
print("*"*10)
l3 = mergeTwoSortedList(l1,l2)
l3.printlist()

