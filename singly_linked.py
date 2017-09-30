class Node(object):
	# Node class, holds data and a forward pointer
	def __init__(self, item, n=None):
		self.obj = item
		self.nxt = n


class SinglyLinkedList(object):

	def __init__(self):
		self.head = None

	def head_add(self, data):
		# prepend to linked list
		n = Node(data)
		if self.head is None:
			self.head = n
		else:
			n.nxt = self.head
			self.head = n

	def remove(self, node):
		# remove a given node
		if self.head == node:
			self.head_pop()
		else:
			curr = self.head
			while curr is not None:
				if curr == node:
					tmp.nxt = curr.nxt
				tmp = curr
				curr = curr.nxt


	def add(self, node, data):
		# add after a given node
		n = Node(data)
		curr = self.head
		while curr is not None:
			if curr == node:
				n.nxt = curr.nxt
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
		prev = None
		while curr is not None:
			if curr.obj == node_value:
				if prev is not None:
					prev.nxt = curr.nxt			 
				else:
					self.head_pop()

			curr = curr.nxt


	def head_pop(self):
		# remove first item
		if self.length() == 1:
			self.head = None
		else:
			self.head = self.head.nxt


	def display(self):
		# print list
		out = '|head| --> '
		curr = self.head
		while curr is not None:
			out += '|{}| --> '.format(curr.obj)
			curr = curr.nxt
		out += '|none|'
		print(out)


if __name__ == '__main__':

	l = SinglyLinkedList()
	l.head_add(1)
	l.head_add(2)
	l.head_add(3)

	l.display()
