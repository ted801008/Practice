def fizzBuzz(n):
	return ['Fizz' * int(not i % 3)+'Buzz' * (not i % 5)+'fizzBuzz' * (not i % 15) or str(i) for i in range(1,n+1)]


print(fizzBuzz(15))

