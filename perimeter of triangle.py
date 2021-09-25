class triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(a,b,c):
        return self.a+self.b+self.c
def main():
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))
    obj = triangle()
    print("The perimeter of the triangle: ",obj.perimeter())
main()
