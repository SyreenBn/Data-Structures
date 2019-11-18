from linked_stack import LinkedStack

class Evaluate:
    def __init__(self):
        self.exp = LinkedStack()

    def postfix_eval(self, str_exp):
        for i in range (0,len(str_exp)):
            if str_exp[i].isdigit():
                self.exp.push(str_exp[i])
            else:
                val1 = self.exp.pop() 
                val2 = self.exp.pop() 
                self.exp.push(str(eval(val2 + str_exp[i] + val1)))
        return int(self.exp.pop())

if __name__ == "__main__":
    e = Evaluate()
    s1 = "23+"
    print(s1, '=', e.postfix_eval(s1))
    s2 = "23+45+*"
    print(s2, '=', e.postfix_eval(s2))
