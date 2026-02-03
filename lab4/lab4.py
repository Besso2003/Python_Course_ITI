from basic_queue import Queue
from advanced_queue import AdvancedQueue, QueueOutOfRangeException

print("=== Basic Queue ===")
q = Queue()
q.insert(10)
q.insert(20)
print("Popped item:", q.pop())  # 10
print("Popped item:", q.pop())  # 20
print("Popped item:", q.pop())  # Warning and None


print("\n=== Advanced Queue ===")

aq1 = AdvancedQueue("myQueue", 3)
aq1.insert(10)
aq1.insert(20)

try:
    aq1.insert(30)
    aq1.insert(40)  # should raise exception
except QueueOutOfRangeException as e:
    print(e)

aq2 = AdvancedQueue("secondQueue", 2)
aq2.insert(100)

try:
    aq2.insert(200)
    aq2.insert(300)  # should raise exception
except QueueOutOfRangeException as e:
    print(e)

AdvancedQueue.save("queues.json")

AdvancedQueue.load("queues.json")

loaded_q1 = AdvancedQueue.get_queue("myQueue")
loaded_q2 = AdvancedQueue.get_queue("secondQueue")

print("Loaded myQueue items:", loaded_q1.items)
print("Loaded secondQueue items:", loaded_q2.items)
