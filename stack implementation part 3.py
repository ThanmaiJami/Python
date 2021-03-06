#method 4
#using singly linked list
"""The linked list has two methods addHead(item) and removeHead() that run in constant time. These two methods are suitable to implement a stack. 
1) getSize()– Get the number of items in the stack.
2) isEmpty() – Return True if the stack is empty, False otherwise.
3) peek() – Return the top item in the stack. If the stack is empty, raise an exception.
4) push(value) – Push a value into the head of the stack.
5) pop() – Remove and return a value in the head of the stack. If the stack is empty, raise an exception."""

#node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    #initializing a stack
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    #string representation of the stack
    
