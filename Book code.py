"""
Question:
Book Code
A abrarian in a central library wants to arrange the new books and keep it in the correct section. For this purpose, he is matching the code of new book with the section code of the library if codes are matching more than 70 percent then he can keep the new book in that particular
section.

Example
Code of new book'ax12nmp

4
Code of section="b12nm

For above 2 codes, common code letters are 1, 2, n, m in sorted order Le.common numbers and then sorted letters, Print common code 12mn and percentage of code matching '57. Since more than 50 percent of code is matching Print The book can be added in section.

Input Format

The first line contains a string s1, code of new book.
The second line contains a string s2, code of section,

Constraints

1s|s1|12|s5000, where [s] means "the length of s
All characters are lower case in the range ascila-z).

Sample Input 1

ccd21
gcd21

Sample Output 1

12cd
80
The book can be added in section

"""
c1 = input()
c2 = input()
#checking the length of two strings
if len(c1) > len(c2):
	n = c1
else:
	n = c2
n_len = len(n)
list = []
#finding same elements
for i in c1:
	for j in c2:
		if i==j:
			list.append(i)
#sorting the list
sort = sorted(list)
#removing duplicates in the list
res = []
for i in sort: 
    if i not in res: 
        res.append(i)
#list to string conversion 
str = ""
y = str.join(res)
print(y)#print 
res_len = len(res)
a = ((res_len*100)//n_len) 
print(a)#print
if a>70:
	print("The book can be added in section")#print 
else:
	print("The book cannot be added in section")#print
