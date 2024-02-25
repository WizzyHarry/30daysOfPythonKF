uses = {'set', 'uses', 'squiglebracket'}
uses.pop()
"""sets are unordered, converting from ____ ends up in randomization"""

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies))
it_companies.add('Twitter')

it_companies.update(['Rapid7', 'RedHat', 'Meta'])

it_companies.discard('Meta')
"""remove can cause compilation errors if item isn't present"""
print(it_companies)


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
C = A.union(B)
print(C)

intersec = A.intersection(B)
print(intersec)
print(A.issubset(B)) #true
print(B.isdisjoint(A)) #false

AB = A.union(B)
BA = B.union(A)
print(AB, BA) #they produced the same output
del A
del B #delete em

