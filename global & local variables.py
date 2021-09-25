message = "This is a global variable"
def greet():
    message = "This is a local variable"
    print(message)
greet()
print(message)

message = "How you doing?"
def greet():
    global message
    message = "What are you doing?"
    print("Message inside the function - ",message)
print("Message outside the function - ",message)
greet()
