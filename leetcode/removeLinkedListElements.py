def removeLinkedListElements(x,val):
	prev = node = x.head
	while(node is not None):
		if(node.data==val):
			prev.next = node.next
			node = node.next
			continue
		prev = node
		node = node.next