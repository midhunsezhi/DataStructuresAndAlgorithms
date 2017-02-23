class BinaryTree(Tree):
""" Abstracty base class for binary tree"""

	def left(self, p):
		raise NotImplementedError('must be implemented by subclass')

	def right(self, p):
		raise NotImplementedError('must be implemented by subclass')

	#Concrete methods

	def sibling(self, p):
		parent = self.parent(p)

		if parent is None:
			return None

		if self.left(parent) == p:
			return self.right(parent)
		else:
			return self.left(parent)

	def children(self, p):
		if self.left(p) is not None:
			yield self.left(p)

		if self.right(p) is not None:
			yield self.right(p)