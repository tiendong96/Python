#FIFO

from collections import deque
#instead of creating an empty variable we call dequeue

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
queue.clear()

if not queue: #empty queue
    print("empty")
