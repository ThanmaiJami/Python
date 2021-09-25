def sum(n1,n2):#positional arguments
    return n1+n2
print("The sum is",sum(1,2))

def sub(n1=10,n2=9):#default arguments
    return n1-n2
print("The diff is",sub(8,4))
#we can use different values instead of default arguments
#there's no problem with it

def mul(b=90,a=30):#keyword arguments
    return a*b
print("The product is",mul(a = 25,b = 2))
#keyword arguments has nothing to do with position...
