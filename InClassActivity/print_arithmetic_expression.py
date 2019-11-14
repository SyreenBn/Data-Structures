"""

Assume a tree data structure representing an arithmetic expression,
such as those constructed above.  Write and test a method printArithExpr()
based on inorder() that prints the expression with parentheses correctly
added to maintain precedence of operations as stored in the tree.  Note that
your method always prints, so you should not pass any argument to your method;
instead, simply print the element of the node on which inorder() would
have called visit().  Your method should not parenthesize individual numbers
or output a pair of parentheses that contain nothing.  You do not need to be
concerned about "nice" spacing of the printed expression.

"""
class ModelTree:
    class Node:
        def __init__(self,element, left = None, right = None):
            self.element = element
            self.left = left
            self.right = right
    def __init__(self,root=None):
        self.root = root

    def printArithExpr(self, visit):
        self._printArithExpr(self.root,visit)

    def _printArithExpr(self,node,visit):
        if node != None:
            if (node.element == "+"
                or node.element == "-"
                or node.element == "*"
                or node.element == "/"):
                print("(",end ="")
                self._printArithExpr(node.left,visit)
                visit(node)
                self._printArithExpr(node.right,visit)
                print(")",end="")
            else:
                self._printArithExpr(node.left,visit)
                visit(node)
                self._printArithExpr(node.right,visit)

r = ModelTree.Node('+')
r.left = ModelTree.Node('*')
r.left.left = ModelTree.Node(1)
r.left.right = ModelTree.Node(2)
r.right = ModelTree.Node(3)
t = ModelTree(r)
def printNode(node):
    print(node.element, end=' ')
print("Print Arithmetic Expression")
t.printArithExpr(printNode)
