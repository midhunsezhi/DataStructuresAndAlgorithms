class DoublyLinkedList:
	class _Node:
		def __init__(self, element, next, prev):
			self._element = element
			self._next = next
			self._prev = prev

	def __init__(self):
		self._header = _Node(None, None, None)
		self._trailer = _Node(None, None, None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def insert_between(self, e, predecessor, successor):
		newest = _Node(e, predecessor, successor)
		predecessor._next = newest
		successor._prev = newest
		self._size += 1
		return newest

	def delete_node(self, node):
		successor = node._next
		predecessor = node._prev

		predecessor._next = successor
		successor._prev = predecessor

		self._size -= 1
		element = node.element
		node._element = node._prev = node._next = None
		return element
