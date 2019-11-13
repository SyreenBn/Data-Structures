class DLL:
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
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_between(self,element_value, pred, succ):
        if self.size == 0:
            self.header = self.Node(element_value, None, self.tailer)
            self.size = self.size + 1 
        elif self.size == 1:
            newNode = self.Node(element_value, pred, succ)
            pred.next = newNode
            self.tailer = newNode
            self.tailer.prev = pred
            self.size = self.size + 1   
        else:
            newNode = self.Node(element_value, pred, succ)
            pred.next = newNode
            succ.prev = newNode
            self.size = self.size + 1

    def delete(self, node):
        current_node = self.header
        if current_node.next == node:
            current_node.next = current_node.next.next
            current_node.next.prev = current_node
        else:
            current_node = current_node.next
            

dlst = DLL()
dlst.insert_between(1,None,None)
print ("Node 1 has been added as header")
dlst.insert_between(2,dlst.header,None)
print ("Node 2 has been added as tailer")
dlst.insert_between(1.5,dlst.header,dlst.tailer)
print ("Node 1.5 has been added between header and tailer")

print ("_____________________")
print ("delet 1.5 node")
dlst.delete(dlst.header.next)
print ("print all element from head -> tail")
print(dlst.header.element)
print(dlst.header.next.element)

