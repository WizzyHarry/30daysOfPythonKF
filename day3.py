age = 20
height = 5.10
compnum = 2 +3j

"""" slope of complex equations """
import math


def generate_table(rows, cols):
    for i in range(1, rows + 1):
        row_values = []
        for j in range(1, cols + 1):
            if j == 1:
                row_values.append(str(i))
            else:
                row_values.append(str(i ** (j - 1)))
        print(" ".join(row_values))

generate_table(5, 5)



def table_generation(romans, collesums):
    for i in range(1, romans + 1):
        romans_values = []
        for j in range(1, collesums + 1):
            if j == 1:
                romans_values.append(str(i))
            else:
                romans_values.append(str(i ** (j - 1)))
        print(" ".join(romans_values))

table_generation(7, 7)
    

print("Enter how old you are in years:")
years = int(input())
time = 365 * 24 * 60 * 60
seconds = years * time
print("You have lived for ", seconds ,"seconds.")



print("Enter hours: ")
hours = int(input())
print("Enter rate per hour: ")
rate = float(input())
week_wage = hours * rate
print("Your weekly earning is " ,week_wage)





value3 = int(9.8)
print(value3)


floor = 7 // 3
value1 = int(2.7)
print(floor)
print(value1)


number = int(input())
def iseven(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
if iseven(number):
    print("even")
else:
    print("odd")



lenghtpy = str(len("pyhton"))
floatlengthpy = float(lenghtpy)
stringlengthpy = str(lenghtpy)
print(floatlengthpy)
print(stringlengthpy)




outstr = str("I hope this course is not full of jargon.")

if 'jargon' in outstr:
    print("yes")
else:
    print("no")
    




string1 = 'python'
string2 = 'dragin'

if 'on' in string1 and 'on' in string2:
    print("On is found in both words")
else:
    print("On is not found in both statements")



lenghtpy = str(len("pyhton"))
print(lenghtpy)

lengthdra = str(len("dragon"))
print(lengthdra)




numin = int(input())
yeleven = numin**2 + 6 * numin + 9
print(yeleven)



x1 = 2
y1 = 2
x2 = 6 
y2 = 10

slope = (y2 - y1) / (x2 - x1)

equdistance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Slope (m): ", slope)
print("Euc Distance: ", equdistance)



print("Enter the width & height of the rectangle")
Rwidth= int(input())
Rheight= int(input())
Rarea = Rwidth * Rheight
Rperim = (Rwidth + Rheight) * 2
print("Area is ", Rarea, "Perimeter is ", Rperim)




print("Enter base: ")
base = float(input())
print("Enter height: ")
triheight = float(input())

areatri = .5 * base * height
print("The area of the triangle is ", areatri)

print("Enter the side lengths of the triangle")
sideA = int(input())
sideB = int(input())
sideC = int(input())

triprim = sideA + sideB + sideC
print("The perimeter of the triangle is ", triprim)

