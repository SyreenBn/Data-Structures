class SLLQueue:
    class Node:
        __slots__ = 'element', 'next'         

        def __init__(self, element, next):
            self.element = element
            self.next = next                 
    #------------------------------- SLLQueue methods -------------------------------                    
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def enqueue(self, element_value):
        if self.head is None:
            self.head = self.Node(element_value, None)
            self.size += 1
        else:
            newNode = self.Node(element_value, self.head) 
            self.head = newNode
            self.size += 1
            
    def first(self):
        if self.is_empty():
            print('Single Linked Queue is empty')
        return self.head.element

    def dequeue(self):
        if self.is_empty():
            print('Single Linked Queue is empty')
        answer = self.head.element
        self.head = self.head.next           
        self.size -= 1
        return answer
    
lst = SLLQueue()
lst.enqueue(1)
print("Node 1 has been added")
print("The head is ", lst.head.element)
lst.enqueue(2)
print("Node 2 has been added")
lst.enqueue(3)
print("Node 3 has been added")
print("The head is ", lst.head.element)
lst.dequeue()
print("Remove one Node")
print("The head is ", lst.head.element)
