from collections import deque

queue = deque()

for i in range(1,11):
    queue.append(i)
queue.pop()
queue.rotate(2)

print(queue)
