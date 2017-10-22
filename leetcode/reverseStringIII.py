def reverseStringIII(str):
	result = ''
	for i in str.split(' '):
		result+=i[::-1]+" "
	print(result)

reverseStringIII("Let's take LeetCode contest")