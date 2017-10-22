def getIntersectionNode(headA,headB):
	curA,curB = headA,headB
	lenA,lenB = 0,0
	while(chA is not None):
		lenA+=1
		chA = chA.next
	while(chB is not None):
		lenB+=1
		chB = chB.next
	curA,curB = headA,headB
	if(lenA>lenB):
		for i in range(lenA-lenB):
			chA = chA.next
	else:
		for i in range(lenB-lenA):
			chB = chB.next

	while(curB!=curA):
		curA = curA.next
		curB = curB.next
	return curA

