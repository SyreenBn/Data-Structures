"""
The Deque (Double-Ended Queue) ADT is, as the name implies, like
a queue that has two "fronts."  So, nodes can be added to and deleted
from either end.  This flexible data structure has many uses.
For instance, a deque can simulate a line of customers in which
certain customers have priority and can therefore move to the front
of the line and in which customers at the end of the line might decide
to stop waiting and leave the line.   Write a class DLLDeque that
implements the Deque ADT with basic methods add_first(), add_last(),
delete_first(), and delete_last().
"""

class DQueue:
        class Node:
                __slots__ = 'element', 'prev', 'next'
        
                def __init__(self, element, prev, next):
                    self.element = element
                    self.prev = prev
                    self.next = next

        def __init__(self):
                self.header = self.Node(None, None, None)
                self.tailer = self.Node(None, None, None)
                self.header.next = self.tailer
                self.tailer.prev = self.header                  
                self.size = 0

        def __len__(self):
                return self._size

        def is_empty(self):
                return self._size == 0

        def first(self):
                return self.header

        def last(self):
                return self.tailer

        def add_first(self, element):
                if self.size == 0:
                        newNode = self.Node(element, None, self.tailer) 
                        self.header = newNode
                        self.size = self.size + 1
                elif self.size == 1:
                        newNode = self.Node(element, None, self.header)
                        self.tailer = self.header
                        self.header = newNode
                        self.tailer.prev = self.header
                        self.size = self.size + 1
                else:
                        newNode = self.Node(element, None, self.header)
                        self.header.prev = newNode
                        self.header = newNode
                        self.size = self.size + 1
                        
        def add_last(self, element):
                if self.size == 0:
                        newNode = self.Node(element, self.header, None) 
                        self.tailer = newNode
                        self.size = self.size + 1
                elif self.size == 1:
                        newNode = self.Node(element, self.tailer, None)
                        self.header = self.tailer
                        self.tailer = newNode
                        self.header.next = self.tailer
                        self.size = self.size + 1
                else:
                        newNode = self.Node(element,self.tailer,None)
                        self.tailer.next = newNode
                        self.tailer = newNode
                        self.size = self.size + 1

        def delete_first(self):
                self.header = self.header.next

        def delete_last(self):
                self.tailer = self.tailer.prev

        def print_first(self):
                current_node = self.header
                print("Print Node element from the header")
                while not (current_node == self.tailer):
                        print(current_node.element)
                        current_node = current_node.next
                print(self.tailer.element)

        def print_last(self):
                current_node = self.tailer
                print("Print Node element from the tailer")
                while not (current_node == self.header):
                        print(current_node.element)
                        current_node = current_node.prev
                print(self.header.element)
                

dqueue = DQueue()
dqueue.add_first(10)
dqueue.add_first(5)
dqueue.add_first(0)
dqueue.print_first()
print("_________________________")
dqueue.print_last()
print("_________________________")

dqueue.add_last(-1)
dqueue.add_last(-2)
dqueue.add_last(-3)
dqueue.print_first()
print("_________________________")
dqueue.print_last()




