"""
Implementation of double ended queues os deques with a circular array
"""

class Deque():
	DEFAULT_CAPACITY = 10

	def __init__(self):
		self._data = [None] * Queue.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		if self.is_empty():
			raise Empty("queue is empty")

		return self._data[self._front]
	def last(self):
		if self.is_empty():
			raise Empty("queue is empty")

		last_index = (self._front + self._size -1) % len(self._data)

		return self._data[last_index]

	def remove_first(self):
		if self.is_empty():
			raise Empty("queue is empty")

		result = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front + 1) % len(self._data)
		self._size -= 1
		return result

	def remove_last(self):
		if self.is_empty():
			raise Empty("queue is empty")

		last_index = (self._front + self._size -1) % len(self._data)
		result = slef._data[last_index]
		self._size -= 1
		return result

	def add_first(self, e):
		if self._size == len(self._data):
			self._resize(2 * len(self._data))

		self._front = (self._front - 1) % len(self._data)
		self._data[self._front] = e
		self._size += 1

	def add_last(self, e):
		if self._size == len(self._data):
			self._resize(2 * len(self._data))

		avail = (self._front + self._size) % len(self._data)
		self._data[avail] = e
		self.size += 1

	def _resize(slef, cap):
		old = self._data
		self._data = [None] * cap
		walk = self._front
		for i in range(self._size):
			self._data[i] = self._data[walk]
			walk = (walk + 1) % self._size
		self._front = 0
