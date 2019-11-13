class SLL:
    class _Node:

        __slots__ = '_element', '_next'         

        def __init__(self, element, next):
            self._element = element
            self._next = next                 

  
    #------------------------------- SLL methods -------------------------------
                        
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def add_to_head(self, element_value):
        if self._head is None:
            self._tail = self._Node(element_value, self._tail)
            self._tail._next = None
            self._head = self._tail
            self._size += 1
        else:
            newNode = self._Node(element_value, self._head) 
            self._head = newNode
            self._size += 1

    def add_to_tail(self, element_value):
        if self._head is None:
            self._tail = self._Node(element_value, self._tail)
            self._tail._next = None
            self._head = self._tail
            self._size += 1
        else:
            newNode = self._Node(element_value, None)
            self._tail._next = newNode
            self._tail = newNode
            self._size += 1
            
    def head(self):
        if self.is_empty():
            print('Single Linked List is empty')
        return self._head._element

    def remove_from_head(self):
        if self.is_empty():
            print('Single Linked List is empty')
        answer = self._head._element
        self._head = self._head._next           
        self._size -= 1
        return answer
    
    def next_to_last (self):
        current_node = self._head
        count = 0
        while count < self._size:
            current_node = current_node._next
            count +=1
        current_node.next = None

    def remove_from_tail(self):
        if self.is_empty():
            print('Single Linked List is empty')
        elif self._size == 1:
            self.remove_from_head()
        else:
            current_node = self._head
            while current_node._next._next is not None:
                current_node = current_node._next
            current_node._next = None
            self._tail = current_node
            self._size -= 1        


lst = SLL()
lst.add_to_head(1)
print("Node 1 has been added to head")
print("The head is ", lst._head._element)
print("The tail is ", lst._tail._element)
lst.add_to_head(2)
print("Node 2 has been added to head")
lst.add_to_head(3)
print("Node 3 has been added to head")
print("The head is ", lst._head._element)
print("The tail is ", lst._tail._element)
lst.remove_from_head()


print("Remove one Node from head")
print("The head is ", lst._head._element)
print("The tail is ", lst._tail._element)

print("Node 0 has been added to tail")
lst.add_to_tail(0)
print("The head is ", lst._head._element)
print("The tail is ", lst._tail._element)

print("Remove one Node from tail")
lst.remove_from_tail()
print("The head is ", lst._head._element)
print("The tail is ", lst._tail._element)

print("New SLL")
lst1 = SLL()
lst1.remove_from_tail()
lst1.add_to_head(1)
print("The head is ", lst1._head._element)
print("The tail is ", lst1._tail._element)
lst1.remove_from_tail()
print(lst1.is_empty())
