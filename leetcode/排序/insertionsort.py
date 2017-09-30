import random
def insertionsort(m1):
	for i in range(1,len(m1)):
		j = i
		data = m1[i]
		while(j>0 and data<m1[j-1]):
			m1[j] = m1[j-1]
			j-=1
		m1[j] = data

SortList = []
for i in range(10):
	SortList.append(random.randint(0,100))
print('Before:',end = " ")
print(SortList)
insertionsort(SortList)
print('After:',end = " ")
print(SortList)
