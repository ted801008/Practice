def countSegments(s):
	count = 0
	for i in s.split(" "):
		count+=1
	return count

print(countSegments("Hello, my name is John"))