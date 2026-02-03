import json

class QueueOutOfRangeException(Exception):
    pass

class AdvancedQueue:
    all_queues = {}

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.items = []
        AdvancedQueue.all_queues[name] = self

    def insert(self, item):
        if len(self.items) >= self.size:
            raise QueueOutOfRangeException(f"Queue '{self.name}' is full!")
        self.items.append(item)
        
    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            print(f"warning: can't pop from empty queue '{self.name}'!")
            return None
        return self.items.pop(0)

    @classmethod
    def get_queue(cls, name):
        return cls.all_queues.get(name)

    @classmethod
    def save(cls, filename):
        data = {name: q.items for name, q in cls.all_queues.items()}
        with open(filename, 'w') as f:
            json.dump(data, f)

    @classmethod
    def load(cls, filename):
        try:
            with open(filename) as f:
                data = json.load(f)
            for name, items in data.items():
                q = AdvancedQueue(name, size=len(items))
                q.items = items
        except FileNotFoundError:
            print("File not found! No queues loaded.")