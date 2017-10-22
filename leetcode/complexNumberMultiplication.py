class Solution(object):
	def complexNumberMultiply(self,a,b):
		element = a.split('+')+b.split("+")
		number = int(element[2])*int(element[0])+int(int(element[3].split("i")[0])*int(element[1].split("i")[0]))*(-1)
		i = int(element[2])*int(element[1].split("i")[0])+int(element[3].split("i")[0])*int(element[0])
		return str(number)+"+"+str(i)+"i"

s1 = Solution()
print(s1.complexNumberMultiply("1+2i","1+3i"))
