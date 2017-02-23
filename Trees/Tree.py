"""
Abstract base class for Tree implementation
"""

class Tree:
	"""
	abstract position class
	"""
	class Position:
		def element(self):
			""" return the element stored at this position """
			raise NotImplementedError('must be implemented by subclass')

		def __eq__(self, other):
			"""return true if other position represents the same location"""
			raise NotImplementedError('must be implemented by subclass')

		def __nq__(self, other):
			return not (self == other) #this calls the previous method


	"""abstract methods"""

	def root(self):
		"""return the position representing tree's root"""
		raise NotImplementedError('must be implemented by subclass')

	def parent(self, p):
		""" return position representing p's parent, return None if root"""
		raise NotImplementedError('must be implemented by subclass')

	def num_children(self, p):
		"""return number of children that position p has"""
		raise NotImplementedError('must be implemented by subclass')

	def childern(self, p):
		"""return the iterations of positions representing p's children"""
		raise NotImplementedError('must be implemented by subclass')

	def __len__(self):
		"""return total number of elements in the tree"""
		raise NotImplementedError('must be implemented by subclass')

	""" concrete methods """

	def is_root(self, p):
		return self.root() == p

	def is_leaf(self, p):
		return self.num_children(p) == 0

	def is_empty(self):
		return len(self) == 0

	def depth(self, p):
		if self.is_root(p):
			return 0
		return 1 + depth(self.parent(p))

	def height(self, p=None):
		if p is None:
			p = self.root()
		if self.is_leaf(p):
			return 0
		return 1 + max(height(c) for c in self.children(p))



