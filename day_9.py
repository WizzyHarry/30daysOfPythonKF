


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

check_1 = 'country'
value_1 = person.get(check_1)
check_2 = 'is_married'
value_2 = person.get(check_2)
if value_1 == 'Finland' and value_2 == True:
    print("Asabeneh Yetayeh lives in Finalnd. He is married.")
else:
    print("wrong")


check = 'skills'
value = person.get(check)
if value != None:
    count = len(person[check])
    num = count // 2
    print(person['skills'][num])
else:
    pass

if value != None:
    if 'Python' in value:
        print(person['skills'])
    else:
        print("No Python skills")
else:
    pass



if 'JavaScript' and 'React' in value:
    print("Front End Developr")
elif 'Node' and 'Python' and 'MongoDB' in value:
    print("Back End Developer")
elif 'React' and 'Node' and 'MongoDB' in value:
    print("Fullstack developer")
else:
    print("Sweatshop worker")




print("add your favorite fruit to the list")

fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = str(input().lower())
if new_fruit in fruits:
    print("This is already a fruit on the list")
else:
    fruits.append(new_fruit)
    print("Added your fruit: ", fruits)





print("What month is it currently? Please use all caps")
month = str(input())

autumn = ['SEPTEMBER', 'OCTOBER', 'NOVEMBER']
winter = ['DECEMBER', 'JANUARY', 'FEBRUARY']
spring = ['MARCH', 'APRIL', 'MAY']
summer = ['JUNE', 'JULY', 'AUGUST']

if month in autumn:
    print("You are in autumn")
elif month in winter:
    print("You are in winter")
elif month in spring:
    print("You are in spring")
elif month in summer:
    print("You are in summer")
else:
    print("Did you spell the month correctly, and is it in CAPS?")



if month == 'SEPTEMBER' or 'OCTOBER' or 'NOVEMBER':
    print("Autumn")
elif month == 'DECEMBER' or 'JANUARY' or 'FEBRUARY':
    print("Winter")
elif month == 'MARCH' or 'APRIL' or 'MAY':
    print("Spring")
elif month == 'JUNE' or 'JULY' or 'AUGUST':
    print("Summer")
else:
    print("Did you spell the month correctly, and use all CAPS?")
#terrible code, if I do it this way i'd have to do month == '' for every month, INSTEAD:
    



print("Input your grade")
grade = int(input())
if grade >= 80 and grade <= 100:
    print("You got an A")
elif grade >= 70 and grade <= 89:
    print("You got a B")
elif grade >= 60 and grade <= 69:
    print("You don't deserve this C")
elif grade >= 50 and grade <= 59:
    print("Drop out, D")
else:
    print("Off to China")



print("Input two numbers, A and B, press enter after each")
A = int(input())
B = int(input())
if A > B:
    print(A, "is greater than ", B)
elif B > A:
    print(B, "is greater than ", A)
else:
    print("Numbers are equal")




print("Enter your age")
your_age = int(input())
print("Enter my age")
my_age = int(input())

if your_age > my_age:
    print("You're older than me!")
elif my_age > your_age:
    print("I'm older than you!")
else:
    print("We are the same age!")




print('qeuifh')

age = int(input())

if age >= 18:
    print("You are old enough to drive")
else:
    num = 18 - age
    print("You need ",num, "more years to learn to drive")


