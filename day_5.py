dry = []
notdry = ['item1', 'item2', 'item3', 'item4', 'item5']
print(len(notdry))
first_item = notdry[0]
print(first_item)
print(notdry[0])
print(notdry[-1], notdry[2])

mixed_data_types = ['David', 'Long', '5.10', 'No', 'Hellnah']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[-1])

middle = len(it_companies) // 2
print(it_companies[middle])

it_companies.append('Cisco')
print(it_companies)

it_companies.insert(3, 'Roc')
print(it_companies)

it_companies[2] = it_companies[2].upper()
print(it_companies)



joined_string = '#; '.join(it_companies)
print(joined_string)

if 'Cisco' in it_companies:
    print("Yes it is in the list")
else:
    print("Hellnah")

print(it_companies.sort())
"""Can you sort text? Is it alphabetically or is that a different command?"""
