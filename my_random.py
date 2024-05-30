from collections import deque

l = list(range(1, 10))
l_deque = deque(l)
print(l_deque)
right_deque = deque(l, 7)
print(right_deque)
right_deque.append(11)
print(right_deque)
right_deque.appendleft(100)
print(right_deque)
right_deque.reverse()
print(right_deque)
right_deque.rotate(3)
print(right_deque)






