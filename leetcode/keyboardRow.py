def findWords(word):
	keyboards = [['q','w','e','r','t','y','i','o','p'],['a','s','d','f','g','h','j','k','l'],['z','x','c','v','b','n','m']]
	line1,line2,line3 = set('qwertyuiop'),set('asdfghjkl'),set('asdfghjkl')
	ret = []
	for i in word:
		w = set(i.lower())
		if(w.issubset(line1) or w.issubset(line2) or w.issubset(line3)):
			ret.append(i)
	return ret

print(findWords(["Hello", "Alaska", "Dad", "Peace"]))