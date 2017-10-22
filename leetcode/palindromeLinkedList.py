class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def isPalindrome(self,head):
		fast,slow = head
		while(fast and fast.next):
			slow = slow.next
			fast = fast.next.next
		stack = [slow.val]
		
		while slow.next:
			slow = slow.next
			stack.append(slow.val)
		while stack:
			if stack.pop() != head.val:
				return False
			head = head.next
		return True

		

