import collections
import math
def numberOfBoomerangs(points):
    nums = 0
    for x1, y1 in points:
        distance = collections.defaultdict(int)
        for x2, y2 in points:
        	dx = abs(x2-x1)
        	dy = abs(y2-y1)
        	d = dx*dx+dy*dy
        	distance[d]+=1

        print(distance)
        nums += sum(n * (n-1) for n in distance.values())

    return nums



print(numberOfBoomerangs([[0,0],[1,0],[1,0]]))



		


