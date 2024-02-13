











company = 'Coding For All'

replacing = company.replace("Coding", "python")
print(replacing)

newline = "Python for Everyone"
newreplace = newline.replace("for Everyone", "for All")
print(newreplace)









"""find"""
discover = company.find("Coding")
if discover != -1:
    print("Found Coding")
else:
    print("Did not find coding")


"""method"""
try:
    is_there = company.index("Coding")
    print("Found Coding")
except ValueError:
    print("Couldn't find")




print(company)
print(len(company))
uppercase = company.upper()
lowercase = company.lower()
capital = company.capitalize()
title = company.title()
swap = company.swapcase()
print(uppercase, lowercase, capital, title, swap)

blankspace = company.find(' ')
cut_str = company[blankspace :]
print(cut_str)


coding = 'coding'
codefor = 'for'
codeall = 'all'
print('{} {} {}' .format(coding, codefor, codeall))


thirty = 'thirty'
days = 'days'
of = 'of'
python = 'pyhton'
thirtydaysofpyhton = "%s %s %s %s" %(thirty, days, of, python)
print(thirtydaysofpyhton)


language = 'Python'
pto = language[0:3:2] 
print(pto) 


first = 'keuth'
last = 'faune'
language = 'german'
long_string = "My name is %s %s. I don't speak %s" %(first, last, language)
print(long_string)

space = ' '
multiline = '''I didn't know you could
make a multiple line string using triple
quotations, I thouhgt it was only comments'''
print(multiline)