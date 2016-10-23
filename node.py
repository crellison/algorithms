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
	