#slicing operator
x = "python"
#method1
res1 = slice(4)
print(x[res1])
res2 = slice(2,6,2)
print(x[res2])
#method2
print("1.",x[::1])
print("2.",x[::2])
print("3.",x[::3])
print("4.",x[::4])
print("5.",x[::-1])
print("6.",x[::-2])
print("7.",x[::-3])
print("8.",x[::-4])
print("9.",x[::-5])
print("10.",x[:1])
print("11.",x[:-1])
print("12.",x[:-2])
print("13.",x[:-3])
print("14.",x[:-4])
print("15.",x[:-5])
print("16.",x[:-6])
print("17.",x[:6])
print("18.",x[5])

x = "Thanmai"
print("1.",x[::1])
print("2.",x[::2])
print("3.",x[::3])
print("4.",x[::4])
print(x[::5])
print(x[::6])
print(x[::7])
print("5.",x[::-1])
print("6.",x[::-2])
print("7.",x[::-3])
print("8.",x[::-4])
print("9.",x[::-5])
print("10.",x[:1])
print("11.",x[:-1])
print("12.",x[:-2])
print("13.",x[:-3])
print("14.",x[:-4])
print("15.",x[:-5])
print("16.",x[:-6])
print("17.",x[:6])
print("18.",x[5])
