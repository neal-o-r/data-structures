
class Node(object):

        def __init__(self, val):
                self.val   = val
                self.left  = None
                self.right = None
        

class BST(object):

        def __init__(self, val=None):
                if val is not None:
                        self.root = Node(val)
                else:
                        self.root = val
        
        def _set_root(self, val):
                self.root = Node(val)


        def insert(self, val):
                if self.root == None:
                        self._set_root(val)
                else:
                        self._insert_node(val, self.root)


        def _insert_node(self, val, node):
                if (val <= node.val):
                        if node.left:
                                self._insert_node(val, node.left)
                        else:
                                node.left = Node(val)
                else:
                        if node.right:
                                self._insert_node(val, node.right)
                        else:
                                node.right = Node(val)


        def find(self, val):
                return self._find_node(val, self.root)


        def _find_node(self, val, node):
                if node == None:
                        return False
                elif val == node.val:
                        return True
                elif val < node.val:
                        return self._find_node(val, node.left)
                else:
                        return self._find_node(val, node.right)


        def traverse(self, node=0):
                if node is None:
                        return
                if node == 0:
                        node = self.root

                self.traverse(node.left)
                print(node.val)
                self.traverse(node.right)


t = BST()
[t.insert(i) for i in [1,10,8,3,4,14,13,7]]
