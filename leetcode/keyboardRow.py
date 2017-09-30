def keyboardRow(x):
	l1,l2,l3 = set('qwertyuiop'),set('asdfghjkl'), set('zxcvbnm')
	ret = []
	for word in x:
		w = set(word.lower())
		if(w.issubset(l1) or w.issubset(l2) or w.issubset(l3)):
			ret.append(word)
	return ret

input = ["Hello", "Alaska", "Dad", "Peace"]
print(keyboardRow(input))