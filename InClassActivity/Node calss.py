class Node:
    def __init__(self, element, prev, next):
        self.element = element
        self.prev = prev
        self.next = next


n1 = Node(1,None, None)
n2 = Node(2, n1, None)
n1.next = n2
n3 = Node(3, n2, None)
n2.next = n3
print ("Element from header")
print(n1.element)
print(n1.next.element)
print(n1.next.next.element)
print ("Element from tailer")
print(n3.element)
print(n3.prev.element)
print(n3.prev.prev.element)
