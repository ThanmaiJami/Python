#sum of first n numbers
#1+2+3+4+...+100=100(101)/2=5050
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)
