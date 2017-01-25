# compute x**n 

def power (x,n):
	if x == 1:
		return 1
	else:
		partial = power(x, n//2)
		result = partial * partial
		if (n % 2 == 1):
			result *= x
		return result