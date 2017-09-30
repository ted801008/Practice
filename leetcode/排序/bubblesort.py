import random
def bubblesort(m1):
	for i in range(len(m1)-1,0,-1):
		for j in range(0,i):
			if(m1[i]<m1[j]):
				t = m1[i]
				m1[i] = m1[j]
				m1[j] = t

SortList = []
for i in range(10):
	SortList.append(random.randint(0,100))
print('Before:',end = " ")
print(SortList)
bubblesort(SortList)
print('After:',end = " ")
print(SortList)

#因為每筆只和右邊的數值比較，所以具有穩定性，複雜度約O(N^2)