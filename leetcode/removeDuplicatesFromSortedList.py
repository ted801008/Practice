def removeDuplicatesFromSortedList(l1):
	node = l1.head
	while node:
		while(node.next and node.next.data = node.data):
			node.next = node.next.next
		node = node.next
	return l1