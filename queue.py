
# a stack
class Stack(object):

        def __init__(self):
                self.data = []

        def push(self, val):
                self.data += [val]

        def pop(self):
                return self.data.pop()
        
        def length(self):
                return len(self.data)
        
s = Stack()
s.push(1)
s.push(2)

print(s.pop())


# a queue
class Queue(object):

        def __init__(self):
                self.data = []

        def enqueue(self, val):
                self.data = [val] + self.data

        def dequeue(self):
                return self.data.pop()

# a queue made of stacks
class Queue_stack(object):

        def __init__(self):
                self.instack = Stack()
                self.outstack = Stack()

        def enqueue(self, val):
                self.instack.push(val)

        def dequeue(self):
                if self.outstack.length() == 0:
                        while self.instack.length():
                                self.outstack.push(self.instack.pop())
                return self.outstack.pop()


q = Queue_stack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
