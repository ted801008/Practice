def validParentheses(string):
	s1 = []
	judge = {"[":"]","{":"}","(":")"}
	for i in string:
		if i in judge.keys():
			s1.append(i) #[(
		elif i in judge.values():
			if s1==[] or i!=judge[s1.pop()]:
				return False
	return True

