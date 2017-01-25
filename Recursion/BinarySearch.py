def binary_search(data, target, high, low):
	if low > high:
		return False
	else:
		mid = (high + low)//2
		if data[mid] == target:
			return True
		elif target > data[mid]:
			binary_search(data, element, high, mid+1)
		else:
			binary_search(data, element, mid-1, low)