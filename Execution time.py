#Calculate Execution time of a  python program
from time import time
start = time()

#python program to create acronyms
word = "Artificial Intelligence"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

#calculating execution time
end = time()
execution_time = end - start
print("Execution Time :",execution_time)

"""OUTPUT:
AI
Execution Time : 0.04809451103210449
"""
