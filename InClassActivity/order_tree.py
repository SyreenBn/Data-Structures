class ModelTree:
    class Node:
        def __init__(self,element, left = None, right = None):
            self.element = element
            self.left = left
            self.right = right
    def __init__(self,root=None):
        self.root = root

    def postorder(self,visit):
        self._postorder(self.root,visit)

    def _postorder(self,node,visit):
        if node != None:
            self._postorder(node.left,visit)
            self._postorder(node.right,visit)
            visit(node)

    def inorder(self, visit):
        self._inorder(self.root,visit)

    def _inorder(self,node,visit):
        if node != None:
            self._inorder(node.left,visit)
            visit(node)
            self._inorder(node.right,visit)

    def preorder(self, visit):
        self._preorder(self.root,visit)
        
    def _preorder(self,node,visit):
        if node != None:
            visit(node)
            self._preorder(node.left,visit)
            self._preorder(node.right,visit) 
        
r = ModelTree.Node('+')
r.left = ModelTree.Node('*')
r.left.left = ModelTree.Node(1)
r.left.right = ModelTree.Node(2)
r.right = ModelTree.Node(3)

t = ModelTree(r)
def printNode(node):
    print(node.element, end=' ')
    
print("postorder")
t.postorder(printNode)
print()
print("inorder")
t.inorder(printNode)
print()
print("preorder")
t.preorder(printNode)

"""
r.right = ModelTree.Node('/', ModelTree.Node(4), ModelTree.Node(5))
print()
t.postorder(printNode)
"""



