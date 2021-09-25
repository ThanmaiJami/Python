class triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a+self.b+self.c
def main():
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))
    obj = triangle(a,b,c)
    print("The perimeter of the triangle: ",obj.perimeter())
main()
