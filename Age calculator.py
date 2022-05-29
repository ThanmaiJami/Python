#Age calculator
def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    age = int((today-dob).days/ 365)
    print(age)
ageCalculator(2001,2,3)

"""OUTPUT:
21
"""


