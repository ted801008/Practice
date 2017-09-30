import random
def shellsort(m1):
	d = 1
	while(d<len(m1)):
		d = d*3+1
	d = (d-1)//3
	while(d>=1):
		d = (d-1)//3
		for i in range(d,len(m1)):
			data = m1[i]
			j = i-d
			while(j>=0 and data<m1[j]):
				m1[j+d] = m1[j]
				j-=d
			m1[j+d] = data

			

SortList = []
for i in range(100):
	SortList.append(random.randint(0,100))
print("Before:",end=" ")
print(SortList)
shellsort(SortList)
print("After:",end=" ")
print(SortList)