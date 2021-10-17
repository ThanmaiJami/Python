#File handling
#Python program to read file word by word
#TEXT FILE: Hello! Welocme to file handling in python...
#Both the text file and python file are on desktop

with open('GFG.txt','r') as file:
    # reading each line    
    for line in file:
        print(line)
        print(line.split())
        
        # reading each word        
        for word in line.split():
            # displaying the words           
            print(word) 
            
#output:
"""
Hello! Welocme to file handling in python...
['Hello!', 'Welocme', 'to', 'file', 'handling', 'in', 'python...']
Hello!
Welocme
to
file
handling
in
python...
"""

#Python program to read character by character from a file
file = open('GFG.txt', 'r')
while 1:
    # read by character
    char = file.read(1)         
    if not char:
        break
    print(char)
file.close()

#output:
"""
H
e
l
l
o
!
 
W
e
l
o
c
m
e
 
t
o
 
f
i
l
e
 
h
a
n
d
l
i
n
g
 
i
n
 
p
y
t
h
o
n
.
.
.
"""
