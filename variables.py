""" Day 2: 30 days of python programming """

first_name = 'John'
last_name = 'Doe'
full_name = 'John Doe'
country = 'Japan'
city = 'Okinawa'
age = 36
year = 2037
is_married = True
is_true = True
is_light_on = False
multiple, varys = 'first', 'second'

print(type(first_name))
print(len(first_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
prod = num_one * num_two
div = num_one / num_two
remain = num_two % num_one
expon = num_one ** num_two
floor = num_one // num_two


print('Raidus: ')
radius = float(input())


pi = 3.14

circum_of_circle = 2 * pi * radius
print(circum_of_circle)

print('Enter your first and last name')
first = str(input())
last = str(input())
print(first, last)