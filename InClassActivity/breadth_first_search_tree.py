"""
In a breadth-first search of a tree, the root of the tree is visited,
then the left child, then the right child, then the left child of the
left child, the right child of the left child, the left child of the
right child, the right child of the right child, the left child of the
left child of the left child, and so on.  Write and test a method bfs(visit)
the carries out a breadth-first search of a tree data structure. Hints:
Breadth-first search is usually implemented using a queue.  The Python
collections module has a deque data structure that provides an efficient
implementation of the Deque ADT and which can be used to construct a queue.

"""

class ModelTree:
    class Node:
        def __init__(self,element, left = None, right = None):
            self.element = element
            self.left = left
            self.right = right
    def __init__(self,root=None):
        self.root = root

    def breadth_first_search(self,visit):
        deque = [self.root]
        while deque:
            cur_node = deque[0]
            deque = deque[1:]
            if cur_node != None:
                visit(cur_node)
                deque.append(cur_node.left)
                deque.append(cur_node.right)


r = ModelTree.Node('+')
r.left = ModelTree.Node('*')
r.left.left = ModelTree.Node(1)
r.left.right = ModelTree.Node(2)
r.right = ModelTree.Node(3)

t = ModelTree(r)
def printNode(node):
    print(node.element, end=' ')
print("bfn")
t.breadth_first_search(printNode)
