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

    def add_first(self, element):
        newNode = Node(element, None, self.header)
        self.header = newNode

    def add_last(self, element):
        newNode = Node(element,self.tailer,None)
        self.tailer = newNode

    def delete_first(self):
        self.header = self.header.next

    def delete_last(self):
        self.tailer = self.tailer.prev

    
