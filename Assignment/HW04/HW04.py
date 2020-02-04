class SortedPiriorityQueue:
 
    def __init__(self):
        self.data = []
        self.size = 0

    def __len__(self):
        return self.size

    def min(self):
        return self.data[0]
        
    def add(self, key, value):
        newest =(key, value)
        if self.size == 0:
            self.data.append(newest)
            self.size += 1
        else:
            i = 0
            while i < self.size:
                to_list = list(self.data[i])
                if key <= to_list[0]:
                    self.data.insert(0,newest)
                    return
                elif key == to_list[0]:
                    self.data.insert(i+1,newest)
                else:
                    self.data.append(newest)
                i = i + 1

    def remove_min(self):
        self.data = self.data[1:]


    def remove_max(self):
        self.data = self.data[:len(self.data)-1]

    def del_element(self,element):
        to_list = element
        for i in range (0,len(self.data)):
            tolist = self.data[i]
            if (tolist[0] == to_list[0]) and (tolist[1] == to_list[1]):
                del self.data[i]
                return
        print ("This element is not in the data")
        
    def print_PQList(self):
        print (self.data)
                    
                
        
lst = SortedPiriorityQueue()
lst.add(4,'A')
lst.add(2,'C')
lst.add(5,'W')
lst.add(5,'S')
lst.print_PQList()

lst.del_element((5,'Q'))

lst.print_PQList()

lst.del_element((5,'S'))
lst.print_PQList()

lst.remove_min()
lst.print_PQList()

lst.remove_max()
lst.print_PQList()

        
