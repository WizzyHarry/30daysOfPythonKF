"""
numbers = (0, 1, 2)
for i in range(11):
    print(i)

for i in range(0, 11, 2):
    print(i)
"""
for i in range (10, 0, -1):
    print(i)


i = 0
while i <= 10:
    print(i)
    i = i + 1

while i > 0:
    print(i)
    i = i -1

for i in range(1, 8):
    print("#" * i)
#In python the astrict when used with strings is a repition operator
    
for i in range(1, 9):
    print(" # " * 8)

x = 0
y = 0

for i in range(0, 11):
    z = x * y
    print(x, " x ", y, " = ", z)
    x += 1
    y += 1


    
#I don't want to spam my computer but these should print up to 100 even and odd only
    """
for i in range(0, 100, 2):
    print(i)

for i in range(0, 101, 2):
    print(i - 1)
    """