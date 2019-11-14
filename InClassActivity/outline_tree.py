"""
The trees we have been studying are called binary trees, because every node
has at most two children.  More generally, tree data structures can have
larger numbers of child nodes.  One purpose of such data structures is to
store outlines (I.A.1.a ...), where the root represents the title of the
outline, the leftmost child of the root contains point I of the outline,
the leftmost child of that child contains point 1A, the second-from-left
child of the 
"""

class OutlineTree:
    class Node:
        def __init__(self,element, children = []):
            self.element = element
            self.children = children
    def __init__(self, root = None):
        self.root = root
        self.level = 0

    def outline(self):
        self._outline(self.root)

    def _outline(self, node):
        if node != None:
            self.printNode(self.printIndentation(self.level),node)
            self.level = self.level + 2
            for i in range (0, len(node.children)):
                self._outline(node.children[i])
            self.level = self.level - 2

    def printNode(self,space, node):
        print(space, node.element)

    def printIndentation(self,num):
        space = ""
        for i in range (0, num):
            space = space + " "
        return space

r = OutlineTree.Node('Title')
r.children = [
   OutlineTree.Node("First point"),
   OutlineTree.Node("Second point"),
   OutlineTree.Node("Third point")
        ]
r.children[0].children = [
   OutlineTree.Node("First point's first subpoint"),
   OutlineTree.Node("First point's second subpoint"),
   OutlineTree.Node("First point's third subpoint")
        ]
r.children[0].children[2].children = [
   OutlineTree.Node("First point's third subpoint's first subpoint"),    
   OutlineTree.Node("First point's third subpoint's second subpoint")
        ]
r.children[1].children = [
   OutlineTree.Node("Second point's first subpoint"),
   OutlineTree.Node("Second point's second subpoint")
        ]
t = OutlineTree(r)
t.outline()
