class Node:
		def __init__(self, element, next):
			self._element = element
			self._next = next

class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self._size = 0


def add_first(L, e):
	newest = Node(e, None)

	newest._next = L.head
	L.head = newest
	L.size += 1

# L is a linked list e is an element
def add_last(L,e):
	newest = Node(e)

	current = L.head

	while current._next != None:
		current = current._next

	current._next = newest
	L.size += 1

def remove_first(L):
	first = L.head

	L.head = first._next
	first._next = None
	L.size -= 1

def remove_last(L):
	current = L.head

	while current._next != None:
		prev = current
		current = current._next

	prev._next = None
	L.tail = prev
	L.size -= 1