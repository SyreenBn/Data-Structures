class SLLStack:
    class _Node:
        __slots__ = '_element', '_next'         

        def __init__(self, element, next):
            self._element = element
            self._next = next                 
    #------------------------------- SLLStack methods -------------------------------                    
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def push(self, element_value):
        if self._head is None:
            self._head = self._Node(element_value, None)
            self._size += 1
        else:
            newNode = self._Node(element_value, self._head) 
            self._head = newNode
            self._size += 1
            
    def top(self):
        if self.is_empty():
            print('Single Linked List is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            print('Single Linked List is empty')
        answer = self._head._element
        self._head = self._head._next           
        self._size -= 1
        return answer
    
lst = SLLStack()
lst.push(1)
print("Node 1 has been added")
print("The head is ", lst._head._element)
lst.push(2)
print("Node 2 has been added")
lst.push(3)
print("Node 3 has been added")
print("The head is ", lst._head._element)
lst.pop()
print("Remove one Node")
print("The head is ", lst._head._element)
