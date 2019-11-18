class ModelStack:
    def __init__(self):
        self.data = tuple()
        self.size = 0
        self.top = 0
    
    def pop(self):
        self.data = self.data[1:len(self.data)-1]
        self.size -= 1
    
    def push(self, e):
        data_list = list(self.data)
        data_list.insert(0,e)
        self.data = tuple(data_list)       
        self.size += 1

    def print_stack(self):
        txt = "("
        data_list = list(self.data)
        for i in data_list:
            txt = txt+str(i)+","

        if len(txt) == 3:
            print(txt + ")")
        else:
            print(txt[0:len(txt)-1]+")")

ms = ModelStack()
ms.push(1)
ms.print_stack()
ms.push(0)
ms.push(-1)
ms.push(-2)

ms.print_stack()


ms.pop()
ms.print_stack()


