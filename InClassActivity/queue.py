"""

Write a Python program that creates a queue and then loops 20 times.
Each time through the loop the program should randomly either enqueue
an integer on the queue (starting at 1, and incrementing each time an
integer is enqueued) or dequeue an integer from the queue and print
the text "serving customer" and then the integer.  If the queue is
empty when a dequeue is attempted, the program should printing "waiting
for the next customer."

"""

import random
import sys
sys.maxsize
class Queue:
    def __init__(self):
        self._data = [] 
        self._size = 0
    def dequeue(self):
        if len(self._data) > 0:
            answer = self._data[0]
            self._data.remove(self._data[0])
            self._size -= 1
            print ("serving customer", answer)
        else:
            print("waiting for the next customer.")
        
    def enqueue(self, e):
        self._data.append(e)
        self._size += 1
    def size(self):
        print(self._size)

    def take_action(self,i):
        counter = 1
        action_num = 1
        while (counter <= i):
            action_num = random.randint(action_num,sys.maxsize)
            if action_num %2 == 0 :
                #print ("Action", counter, "enqueue")
                self.enqueue(counter)
                counter = counter + 1
            else:
                #print ("Action", counter,"dequeue")
                self.dequeue()
                counter = counter + 1

q = Queue()
q.take_action(20)
