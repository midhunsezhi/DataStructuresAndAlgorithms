"""
implementation of Stack using Python's list class. "Adapter Pattern".
"""

class Stack():
	def __init__(self):
		self._data = []

	def __len__(self):
		return len(self._data)

	def push(self, item):
		self._data.apend(item)

	def isEmpty(self):
		return len(self._data) == 0

	def pop(self):
		if self.isEmpty():
			raise Empty('Stack is empty')					# custom Empty exception to throw an error
		return self._data.pop()

	def top(self):
		if self.isEmpty():
			raise Empty('Stack is empty')					# custom Empty exception to throw an error
		return self._data[-1]

