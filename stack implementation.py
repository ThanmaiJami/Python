#Stack implementation
#method 1
#list
stack = []
#append() function to push elements into the stack
stack.append('a')
stack.append('b')
stack.append('c')
print("Initial stack -", stack)
print("Elements popped from stack :")
#pop() function for popping elements in LIFO order
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("Stack after elements are popped -", stack)

#method 2
"""Deque is preferred over the list in the cases where we 
need quicker append and pop operations from both the ends 
of the container, as deque provides an O(1) time complexity 
for append and pop operations as compared to list which provides 
O(n) time complexity. """
from collections import deque
stack = deque()
#append() function to push elements into the stack
stack.append('a')
stack.append('b')
stack.append('c')
print("Initial stack -", stack)
print("Elements popped from stack :")
#pop() function for popping elements in LIFO order
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("Stack after elements are popped -", stack)
