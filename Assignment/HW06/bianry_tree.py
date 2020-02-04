class ModelBinarySearchTree:
    class Node:
        def __init__(self, element, parent=None, left=None, right=None):
          self.element = element
          self._left = left
          self._right = right
          self._parent = parent
          self._height = 0

        def left_height(self):
          return self._left._height if self._left is not None else 0          
        def right_height(self):
          return self._right._height if self._right is not None else 0        

    # Constructor for ModelBinarySearchTree    
    def __init__(self, root=None):
        self._root = root
    
    def insert(self, value):  # this is the function that gets called, pay attention that we're not sending `root`
      if self._root is None:
        self._root = self.Node(value)
      else:
        self._insert(self._root, value) # here's the call to a "private" function to which we are passing nodes down, starting from root

    def _insert(self, node, value):
      if value < node.element:  # we know that `node` cannot be None - so it's safe to check its value! 
        if node._left:
          self._insert(node._left, value) # the recursive call is done only when `node.left` is not None
        else:
          node._left = self.Node(value,node)  # direct assignment
      else:
        if node._right:
          self._insert(node._right, value)
        else:
            node._right = self.Node(value,node)  # direct assignment


    def _relink(self, parent, child, make_left_child):
        if make_left_child:                     # make it a left child
          parent._left = child
        else:                                   # make it a right child
          parent._right = child
        if child is not None:                   # make child point to parent
          child._parent = parent
        
    def _rotate(self, node):
        x = node
        y = x._parent             # we assume this exists
        z = y._parent             # grandparent (possibly None)
        if z is None:            
            self._root = x          # x becomes root
            x._parent = None        
        else:
            self._relink(z, x, y is z._left)     # x becomes a direct child of z
          
        # now rotate x and y, including transfer of middle subtree
        if x is y._left:
            self._relink(y, x._right, True)      # x._right becomes left child of y
            self._relink(x, y, False)            # y becomes right child of x
        else:
            self._relink(y, x._left, False)      # x._left becomes right child of y
            self._relink(x, y, True)             # y becomes left child of x

    def _restructure(self, node):
        x = node
        y = x._parent
        z = y._parent
        if (x is y._right) == (y is z._right):   # matching alignments
          self._rotate(y)                        # single rotation (of y)
          return y                               # y is new subtree root
        else:                                    # opposite alignments
          self._rotate(x)                        # double rotation (of x)     
          self._rotate(x)
          return x                               # x is new subtree root
          
    def _recompute_height(self, p):
      p._height = 1 + max(p.left_height( ), p.right_height( ))
  
    def _isbalanced(self, p):
      return abs(p.left_height( ) - p.right_height( )) <= 1
    
    def _tall_child(self, p, favorleft=False): # parameter controls tiebreaker
      if p.left_height( ) + (1 if favorleft else 0) > p.right_height( ):
        return p._left
      else:
        return p._right
        
    def _tall_grandchild(self, p):
      child = self._tall_child(p)
      # if child is on left, favor left grandchild; else favor right grandchild
      alignment = (child == p._left)
      return self._tall_child(child, alignment)  
        
    def find_leaf(self,node):
        while node._left != None:
            node = node._left
        return node

    def _rebalance(self, node):
      while node is not None:
        old_height = node._height
        if not self._isbalanced(node):
          node = self._restructure(self._tall_grandchild(node))
          self._recompute_height(node._left)
          self._recompute_height(node._right)
        self._recompute_height(node)
        if node._height == old_height:
          node = None
        else:
          node = node._parent
          
    def inorder(self):
        self._inorder(self._root)

    def _inorder(self,node):
        if node != None:
            self._inorder(node._left)
            print(node.element, end = " ")
            self._inorder(node._right)
        


    def delete(self, node):
        if node._left == None and node._right == None:
            if node._parent._left == node:
                node._parent._left = None
            else:
                node._parent._right = None            
        elif node._left != None and node._right == None:
            if node._parent._left == node:
                newNone = node._left
                node._left = None
                node._parent._left = newNone      
            else:
                newNone = node._left
                node._left = None
                node._parent._right = newNone
            self._rebalance(node)
        elif node._left == None and node._right != None:
            if node._parent._left == node:
                newNone = node._right
                node._left = None
                node._parent._left = newNone      
            else:
                newNone = node._right
                node._left = None
                node._parent._right = newNone
            self._rebalance(node)
        else:
            temp = self.find_leaf(node)
            if node._parent._left == node:
                node._parent._left.element = temp.element
                self.delete(temp)
            else:
                node._parent._right.element = temp.element
                self.delete(temp)
            self._rebalance(node)
            
t = ModelBinarySearchTree()
t.insert(44)
t.insert(17)
t.insert(78)
t.insert(38)
t.insert(50)
t.insert(88)
t.insert(48)
t.insert(62)
t.insert(46)
t.inorder()
print()
t.delete(t._root._right._left)
t.inorder()
