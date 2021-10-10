#method 3
#queue
#Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the put() function and get() takes data out from the Queue. 
"""There are various functions available in this module: 
1) maxsize – Number of items allowed in the queue.
2) empty() – Return True if the queue is empty, False otherwise.
3) full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
4) get() – Remove and return an item from the queue. If the queue is empty, wait until an item is available.
5) get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
6) put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
7) put_nowait(item) – Put an item into the queue without blocking.
8) qsize() – Return the number of items in the queue. If no free slot is immediately available, raise QueueFull."""

from queue import LifoQueue
#initializing the stack
stack = LifoQueue(maxsize = 3)
#qsize() function to show number of elements in the stack
print("The number of elements in the stack are :", stack.qsize())
#put() function to push elements in the stack
stack.put('9')
stack.put('abcc')
stack.put('f')
print("Full :",stack.full())
print("stack size :",stack.qsize())
#get function to pop elements
#LIFO order
print(stack.get())
print(stack.get())
print(stack.get())
print("Stack is empty :",stack.empty())
