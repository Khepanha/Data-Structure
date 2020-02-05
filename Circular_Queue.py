class CircularQueue(object):
    def __init__(self):
        self.queue = list()
        self.size = 3
        self.head = 0
        self.tail = 0
    def enqueue(self):
        if self.size == (self.size - 1):
            return 'Queue is full'
        else: 
            while len(self.queue) != self.size:
                data = int(input('enqueue: '))
                self.queue.append(data)
            print ('Circular Queue: ')
            return self.queue
    def dequeue(self):
        if self.size == 0:
            return 'Queue is empty'
        else:
            self.queue.pop(0)
            print(self.queue)
            return self.enqueue()          
obj = CircularQueue()
print (obj.enqueue())
print (obj.dequeue())