from doubly_linked_list import DoublyLinkedList 
class TextEdit:
    def __init__(self):
        self.text = DoublyLinkedList()
        self.switch = 0

    def insert(self,c):
        if self.switch == 0:
            self.text.insert_at_start(c)
            self.switch = self.switch + 1
        elif self.switch == self.text.__len__():
            self.text.insert_at_end(c)
            self.switch = self.switch + 1
        else:
            counter = 0
            current_node = self.text.header
            while counter < self.switch:
                current_node = current_node.next
                counter = counter + 1
            self.text.insert_between(c, current_node.prev, current_node)
            self.switch = self.switch + 1
   
    def delete(self):
        counter = 0
        current_node = self.text.header
        while counter != self.switch:
            current_node = current_node.next
            counter = counter + 1
        if self.switch < self.text.__len__():
            self.text.delete_between(current_node)
            if self.switch == 1:
                self.switch = self.switch - 1
        
        
       
    def left(self):
        if self.switch != 0:
            self.switch = self.switch - 1

    def right(self):
        self.switch = self.switch + 1
        
    def print(self):
        
        current_node = self.text.header
        count = 0
        space = ""
        while count < self.text.__len__():
            if count != self.switch-1:
                space = space + " "
            else:
                space = space + "^"
                
            print(current_node.element, end = "")
            current_node = current_node.next
            count = count + 1
        if (self.switch == 0):
            print("\n^")
        else:
            print("\n",space)

        

t = TextEdit()
t.insert('a')
t.insert('b')
t.print()

t.left()

t.print()

t.insert('c')
t.insert('d')
t.print()

t.delete()
t.delete()
t.print()

for i in range(4):
    t.left()
t.delete()
t.print()
