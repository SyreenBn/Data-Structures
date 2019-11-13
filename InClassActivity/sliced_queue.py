"""
Write a class SlicedQueue that uses the list append() method and list
slicing to implement the same functionality as Queue.  Note: You should
not need DEFAULT_CAPACITY class variable or the _size or _front attributes.
"""

class SlicedQueue:
    def __init__(self):
        self._data = [] 
        self._size = 0
    def dequeue(self):
        answer = self._data[0]
        self._data.remove(self._data[0])
        self._size -= 1
        return answer
    def enqueue(self, e):
        self._data.append(e)
        self._size += 1
    def size(self):
        print(self._size)

q = SlicedQueue()

for i in range(100000):
    q.enqueue(i)
for i in range(100000):
    q.dequeue()
