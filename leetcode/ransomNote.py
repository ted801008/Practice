def canConstruct(ransomNote,magazine):
	ransomNote = list(ransomNote)
	for i in magazine:
		if i in ransomNote:
			ransomNote.remove(i)
	if (len(ransomNote)==0):
		return True
	else:
		return False

print(canConstruct("a","b"))