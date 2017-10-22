class IntList(object):
	value = 0
	next = None
	def solution(L):
		node = L.head
		count = 0
		if node is None:
			return 0
		else:
			while(node is not None):
				count+=1
				node = node.next
		return count

