memo = {}

def fib(n):
	"""Computes the nth fibonacci number recursively"""
	if memo.get(n) is not None:
		return memo[n]
	if (n < 2):
		return 1
	fibn = fib(n-1) + fib(n-2)
	memo[n] = fibn
	return fibn

if __name__ == '__main__':
	print fib(100)