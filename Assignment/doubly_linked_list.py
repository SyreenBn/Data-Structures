class Node:
    def __init__(self, element, prev, next):
        self.element = element
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.header = Node(None, None, None)
        self.tailer = Node(None, None, None)
        self.header.next = self.tailer
        self.tailer.prev = self.header                  
        self.size = 0

    def __len__(self):
        """Return the number of elements in the list."""
        return self.size

    def is_empty(self):
        """Return True if list is empty."""
        return self.size == 0

    def insert_in_emptylist(self, element):
        if self.header.element is None:
            new_node = Node(element, None, self.tailer)
            self.header = new_node
            self.tailer.prev = self.header
            self.size = self.size + 1
        else:
            print("list is not empty")
            
    def insert_in_one_element_list(self, element):
        new_node = Node(element, None, self.header)
        self.tailer = self.header
        self.header = new_node
        self.header.next = self.tailer
        self.tailer.prev = self.header
        self.size = self.size + 1  
        
    def insert_between(self, element, start, end):
        if start.element is None and end.element is None:
            self.insert_in_emptylist(element)
        elif start.element != None and end.element is None:
            self.insert_in_one_element_list(element)
        else:
            new_node = Node(element, start, end)
            start.next = new_node
            end.prev = new_node
            self.size = self.size + 1

    def insert_at_start (self, element):
        if self.header.element is None and self.tailer.element is None:
            self.insert_in_emptylist(element)
        elif self.header.element != None and self.tailer.element is None:
            self.insert_in_one_element_list(element)
        else:
            new_node = Node(element, None, self.header)
            self.header.prev = new_node
            self.header = new_node
            self.size = self.size + 1
        
    def insert_at_end(self, element):
        if self.header.element is None and self.tailer.element is None:
            self.insert_in_emptylist(element)
        elif self.header.element != None and self.tailer.element is None:
            new_node = Node(element, self.header, None)
            self.header.next = new_node
            self.tailer = new_node
            self.size = self.size + 1
        else:
            new_node = Node(element, self.tailer, None)
            self.tailer.next = new_node
            self.tailer = new_node
            self.size = self.size + 1
                
    def display_list(self):
        if self.header.element is None:
            print("List has no element")
            return
        elif self.tailer.element is None:
            print(self.header.element , end = " ")
        else:
            n = self.header
            while n is not None:
                print(n.element , end = " ")
                n = n.next
        print()
             
    def delete_at_start(self):
        if self.header is None:
            print("The list has no element to delete")
            return 
        if self.header.next is None:
            self.start_node = None
            self.size = self.size - 1
            return
        self.header = self.header.next
        self.header.prev = None
        self.size = self.size - 1

    def delete_at_end(self):
        if self.header is None:
            print("The list has no element to delete")
            return 
        if self.header.next is None:
            self.start_node = None
            return
        n = self.tailer
        self.tailer = n.prev
        self.tailer.next = None
        self.size = self.size - 1

    def delete_between(self, node):
        if node.prev is None and node.next is not None:
            self.delete_at_start()
        elif node.next is None and node.prev is not None:
            self.delete_at_end()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size = self.size - 1


"""
new_linked_list = DoublyLinkedList()
new_linked_list.insert_in_emptylist(50)
new_linked_list.display_list()
new_linked_list.insert_at_start(10)
new_linked_list.insert_at_start(5)
new_linked_list.insert_at_start(18)
new_linked_list.insert_at_end(29)
new_linked_list.insert_at_end(39)
new_linked_list.insert_at_end(49)
new_linked_list.display_list()
new_linked_list.delete_at_start()
new_linked_list.delete_at_end()
new_linked_list.display_list()




"""
