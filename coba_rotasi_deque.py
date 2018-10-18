from collections import deque

items = deque()
items.append('1') # deque == [1, 2, 3]
items.append('2') # deque == [1, 2, 3]
items.append('3') # deque == [1, 2, 3]
print(items[0])
items.rotate(1) # The deque is now: [3, 1, 2]
print(items[0])