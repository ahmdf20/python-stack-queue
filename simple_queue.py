from collections import deque

queue = deque([1,2,3,4,5])
print(f"queue = {queue}")

for i in range(len(queue)+1, 8):
  queue.append(i)
  print(f"queue input : {i}")
  print(f"queue = {queue}")

out = queue.popleft()
print(f"queue out : {out}")
print(f"queue = {queue}")