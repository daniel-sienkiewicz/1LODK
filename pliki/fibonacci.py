def fib(n):
	"""Return a list containing the Fibonacci series up to n."""
	
	result = []
	a, b = 0, 1

	while a < n:
		result.append(a)
		a, b = b, a + b
	return result


f100 = fib(100)

print f100
print fib.__doc__

