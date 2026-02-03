class Queue:
    def __init__(self):
        self.items = []
    
    def insert(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            print("Warning: can't pop from empty queue!")
            return None
        return self.items.pop(0)

    