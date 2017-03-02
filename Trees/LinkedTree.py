class LinkedTree(Tree):
	"""Linked representation of a binary tree"""

	class _Node:
		def __init__(self, element, parent=None, children=[]):
			self._element = element
			self._parent = parent
			self._children = children

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

	#------------ linked tree constructor ----------------#

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

	def children(self, p):
		node = self._validate(p)
		return [self._make_position(childNode) for childNode in node._children]

	def num_children(self, p):
		node = self._validate(p)
		return len(node._children)
