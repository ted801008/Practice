def studentAttendanceRecord(str):
	score = {'A':0,'L':0,"P":0}
	for i in str:
		score[i]+=1
	if(score['A']>1 or score['L']>2):
		return False
	return True

print(studentAttendanceRecord("PPALLL"))
