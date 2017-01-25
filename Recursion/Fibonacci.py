#print the nth fibonacci number. the function will return f(n) and f(n-1)
def fibonacci(n):
	if n <=1:
		return (n,0)
	else:
		(a,b) = fibonacci(n-1)
		return (a+b, a)