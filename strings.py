string = "He said \"What\'s there\""
print(string)
#we use  back slash when these trivial sentences are used as strings...


#concatenation
text1 = "Python"
text2 = "Programmming"
res1 = text1 + " " + text2
print(res1)
#multiply string
res2 = text1*4
print(res2)
print(text2*5)
#iterating through string
for character in res1:
    print(character)
#length of string
res3 = len(text1)
print("The length of the text1 is ",res3)
#print("on" in text1) to check the mentioned string is present in text1 or not
print("on" in text1)
print("Adaf"in text2)


#string methods
s = "I like Python"
res1 = s.lower()#lowercase method
res2 = s.upper()#uppercase method
print("lower: ",res1, "upper: ",res2)
#to find index of "python" substring in s
res3 = s.find("Python")
print(res3)
#replace method
res4 = s.replace("Python","Java")
print(res4)
