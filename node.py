class Node:
	def __init__(self, head=None):
		self.head = head
		self.tail = None
	# basic getters
	def getHead(self):
		return self.head
	def getTail(self):
		return self.tail
	# basic setters
	def setHead(self, value):
		self.head = value
	def setTail(self, value):
		self.tail = Node(value)
	# removals
	def amputateTail(self):
		self.tail = None
	def decapitate(self):
		self.head = self.getTail().head if self.getTail() is not None else None
		if self.head is not None:
			self.tail = self.getTail() if self.getTail() is not None else None
		else:
			self.tail = None
	# print it out
	def toString(self):
		output = str(self.head)
		tail = self.tail
		while tail is not None:
			output += ' > ' + str(tail.getHead())
			tail = tail.getTail()
		return output