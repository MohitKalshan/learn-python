# List as a Queue
# enqueue/offer -> add
# dequeue -> remove

queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

# Dequeue
queue.pop(0)

print(queue)




from collections import deque

queue = deque()

# Enqueue (O(1))
queue.append(10)
queue.append(20)
queue.append(30)

# Dequeue (O(1))
queue.popleft()

print(queue)