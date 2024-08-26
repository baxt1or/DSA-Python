

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        return self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            return IndexError("Empty")
        return self.queue.pop()

    def peek(self):
        if len(self.queue) != 0:
            return self.queue[-1]
        else:
            raise IndexError("Empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
    def __str__(self) -> str:
        return str(self.queue)


q = Queue()
q.enqueue("Hello")
q.enqueue("Alex")
print(q.is_empty())
print(q.dequeue())
print(q.size())
print(q)