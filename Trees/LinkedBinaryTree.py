class LinkedBinaryTree(BinaryTree):
	"""Linked representation of a binary tree"""

	class _Node:
		def __init__(self, element, parent=None, left=None, right=None):
			self._element = element
			self._parent = parent
			self._left = left
			self._right = right

	class Position(BinaryTree.Position):
		"""An abstraction representing the location of a single element."""
		def __init__(self, container, node):
			self._container = container
			self._node = node

		def element(self):
			"""return the element stored in the Node reffered by this position"""
			return self._node._element

		def __eq__(self, other):
			"""return true if other is a position refering the same node"""
			return type(self) == type(other) and self._node == other._node

	def _validate(self, p):
		"""return associate node if p is a valid position"""
		if not isinstance(p, self.Position):
			raise TypeError('p must be a proper Position type')

		if p._container is not self:
			raise ValueError("p doesn't belong to this container")

		if p._node._parent is p._node:	#deprecated node
			raise ValueError(" p is no longer valid")

	def _make_position(self, node):
		"""Return position instance of given node"""
		return self.Position(self, node) if node is not None else None

	#------------ binary tree constructor ----------------#

	def __init__(self):
		"""create an initially empty binary tree"""
		self._root = None
		self._size = 0

	#-------------- public accessors ----------------
	def __len__(self):
		return self._size

	def root(self):
		return self._make_position(self._root)

	def parent(self, p):
		node = self._validate(p)
		return self._make_position(node._parent)

	def left(self, p):
		node = self._validate(p)
		return self._make_position(node._left)

	def right(self, p):
		node = self._validate(p)
		return self._make_position(node._right)

	def num_children(self, p):
		node = self._validate(p)
		count = 0
		if self.left(p) is not None:
			count += 1
		if self.right(p) is not None:
			count += 1

		return count

	#---------------- Update methods --------------
	""" The following methods can be mate public if required by the clildren classes by adding a wrapper around these methods """
	def _add_root(self, e):
		"""place element e at the root and return the new Position"""
		if self._root is not None:
			raise ValueError('Root Exists')

		self._size = 1
		self._root = self._Node(e)
		return self._make_position(self._root)

	def _add_left(self, p, e):
		"""place element e at left child of p and return new Position"""

		node = self._validate(p)

		if node._left is not None:
			raise ValueError('Left child exists')
		self._size += 1
		node._left = self._Node(e, node)
		return self._make_position(node._left)


	def _add_right(self, p, e):
		"""place element e at right child of p and return new Position"""

		node = self._validate(p)

		if node._right is not None: raise ValueError('Right child exists')
		self._size += 1
		node._right = self._Node(e, node)
		return self._make_position(node._right)

	def _replace(self, p, e):
		"""replace the elemnt at p with e and return old element"""
		node = self._validate(p)

		old = node._element
		node._element = element
		return old

	def _delete(self, p):
		""" replace node at p with its child node, if any
			return the old element at p
			raise value error if p has 2 children or is invalid
		"""

		node = self._validate(p)

		if self.num_children(node) == 2:
			raise ValueError('p has 2 children')

		child = node._left if node._left is not none else node._right

		if child is not None:
			child.parent = node._parent

		if node is self._root:
			self._root = child
		else:
			parent = node._parent
			if node is parent._left:
				parent._left = child
			else:
				parent._right = child

		node._parent = node #convention for deprecated nodes

		return node._element

	def _attach(self, p, t1, t2):
		"""add subtree t1 as left child and t2 as right child of positipn p if its a leaf or throw value error"""

		node = self._validate(p)

		if not self.is_leaf(p):
			raise ValueError('p is not a leaf')

		if not (type(self) is type(t2) is type(t2)):
			raise TypeError('T1 and T2 are not the cureent tree type')

		self._size += len(t1) + len(t2)

		if not t1.is_empty():
			node._left = t1._root
			t1._root._parent = node
			t1._root = None
			t1._size = 0

		if not t2.is_empty():
			node._right = t2._root
			t2._root._parent = node
			t2._root = None
			t2._size = 0
