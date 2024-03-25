"""
def add_two(num_one, num_two):
    sum = num_one + num_two
    return sum

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
result = add_two(x, y)
print("The sum is: ", result)


def circle(radius):
    rad = radius * radius
    area = rad * 3.14
    return area

radius = float(input())
area = circle(radius)
print("The area of the circle is: ", area)

"""

def add_all_nums(*args):
    total = 0
    while True:
        num_input = input("Enter a number, enter sto when finished: ")
        if num_input.lower() == 'sto': #end input isn't working?
            break
        try:
            num = float(num_input)
            total += num
        except ValueError:
            print("Please make sure your arguement is a number")
    return total

print("The sum of the numbers is: ", add_all_nums)