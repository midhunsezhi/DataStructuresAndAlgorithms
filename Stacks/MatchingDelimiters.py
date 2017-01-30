def is_matched(expression):
	lefty ='{[('
	righty = '}[)'

	s = Stack()

	for c in expression:
		if c in lefty:
			s.push(c)

		elif c in righty:
			if s.is_empty():
				return False
			elif righty.index(c) != lefty.index(s.pop()):
				return False

	return s.is_empty()
