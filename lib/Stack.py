class Stack:

    def __init__(self, items = [], limit = 100):
        if items is None :
         items = []
        self.items = items
        self.limit = limit
        

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) >= self.limit:
            return
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return len(self.items) -1 - self.items.index(target)
        return -1