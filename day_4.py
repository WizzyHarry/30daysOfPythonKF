





import cmath


print('{0} + {1} = {2}'.format(8, 6, 8 + 6))
print('{0} - {1} = {2}'.format(8, 6, 8 - 6))
print('{0} * {1} = {2}'.format(8, 6, 8 * 6))
print('{0} / {1} = {2}'.format(8, 6, 8 / 6))
print('{0} % {1} = {2}'.format(8, 6, 8 % 6))
print('{0} // {1} = {2}'.format(8, 6, 8 // 6))
print('{0} ** {1} = {2}'.format(8, 6, 8 ** 6))




sentence = 'You cannot end a sentence with because because because is a conjunction'
company = 'Coding For All'


tabseq = """Name\t\tAge\t\tCountry\t\tCity
Asabeneh\t250\t\tFinland\t\tHelsinki"""
print(tabseq)



widebody = ' Coding For All '
snip = widebody.strip(' ')
print(snip)


list_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joining = ' # '.join(list_list)
print(joining)

longstuff = "I am enjoying this challenge. I just wonder what is next."
print(longstuff)

longbutcutstuf = "I am enjoying this challenge.\nI just wonder what is next."
print(longbutcutstuf)



subcomp = 'Coding'
subtwocomp = 'coding'

if company.startswith(subcomp):
    print("Yes it does start with substring Coding")
else:
    print("nO")

if company.startswith(subtwocomp):
    print("Yes it does start with the substring coding")
else:
    print("L substring")


companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
splitting = companies.split(',')
print(splitting)


position = company.rfind('l')
print(position)

whereat = sentence.find('because')
print(whereat)
wherearthou = sentence.rfind('because')
print(wherearthou)
chop = sentence.slice('because')
print(chop)


"""I did something wrong here"""
"""mastersplinter = sentence.slice()
thesplit = [word for word in mastersplinter if word != 'because']
remerge = ' '.join(thesplit)
print(remerge)"""



placement = company.index('C')
print(placement)

placing = company.index('F')
print(placing)


abbrev = ''.join(word[0] for word in company.split(' '))
print(abbrev)

two = 'Python for All'
shorten = ''.join(word[0] for word in two.split(' '))
print(shorten)

print(company[0])
print(company[-1])
print(company[10])



splitter = company.split(' ')
print(splitter)


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
