class Node(object):
	# Node class, holds data and a forward and backward pointer
	def __init__(self, item, p=None, n=None):
		self.obj = item
		self.prv = p
		self.nxt = n


class DoublyLinkedList(object):
	'''
	Doubly Linked List Class
	'''
	def __init__(self):
		# initialise empty list
		self.head = None
		self.tail = None


	def tail_add(self, data):
		# append to linked list
		n = Node(data)
		if self.head is None:
			self.head = self.tail = n
		else:
			n.prv = self.tail
			self.tail.nxt = n
			self.tail = n


	def head_add(self, data):
		# prepend to linked list
		n = Node(data)
		if self.head is None:
			self.head = self.tail = n
		else:
			n.nxt = self.head
			self.head.prv = n
			self.head = n


	def remove(self, node):
		# remove a given node
		if self.head == node:
			self.head_pop()
		elif self.tail == node:
			self.tail_pop()
		else:
			curr = self.head
			while curr is not None:
				if curr == node:
					curr.prv.nxt = curr.nxt
					curr.nxt.prv = curr.prv
				curr = curr.nxt


	def add(self, node, data):
		# add after a given node
		n = Node(data)
		curr = self.head
		while curr is not None:
			if curr == node:
				n.nxt = curr.nxt
				n.prv = curr
				curr.nxt = n
			curr = curr.nxt
			

	def length(self):
		# get length
		c = 0
		curr = self.head
		while curr is not None:
			c += 1
			curr = curr.nxt

		return c


	def remove_value(self, node_value):
		# remove all appearances of value
		curr = self.head
		while curr is not None:
			if curr.obj == node_value:
				if curr.prv is None and curr.nxt is None:
					self.head = None
					self.tail = None
				elif curr.prv is not None:
					curr.prv.nxt = curr.nxt
					if curr.nxt is not None:
						curr.nxt.prv = curr.prv
					else:
						curr.nxt = None

				else:
					self.head = curr.nxt
					curr.nxt.prv = None
 
			curr = curr.nxt


	def head_pop(self):
		# remove first item
		if self.length() == 1:
			self.head = None
			self.tail = None

		else:
			self.head.nxt.prv = None
			self.head = self.head.nxt


	def tail_pop(self):
		# remove last item
		if self.length() == 1:
			self.head = None
			self.tail = None

		else:
			self.tail.prv.nxt = None
			self.tail = self.tail.nxt


	def display(self):
		# print list
		out = '|head| <--> '
		curr = self.head
		while curr is not None:
			out += '|{}| <--> '.format(curr.obj)
			curr = curr.nxt
		out += '|tail|'
		print(out)


if __name__ == '__main__':
	
	l = DoublyLinkedList()
	l.tail_add(1)
	l.tail_add(2)
	l.tail_add(1)

	l.display()

