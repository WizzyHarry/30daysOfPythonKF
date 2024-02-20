
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

mid_find = len(countries) // 2
middle_country = countries[mid_find] if len(countries) % 2 != 0 else [countries[mid_find] - 1], countries[mid_find]
print(middle_country)


if len(countries) % 2 == 0:
    first_half = countries[:mid_find]
    second_half = countries[mid_find:]
else:
    first_half = countries[:mid_find + 1]
    second_half = countries[mid_find + 1:]

print(first_half)
print(second_half)







ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
min_age = min(ages)
max_age = max(ages)
total_age = sum(ages)
avg_age = total_age / len(ages)
age_range = max_age - min_age
min_avg = abs(min_age - avg_age)
max_avg = abs(max_age - avg_age)


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

ult_list = front_end + back_end
print(ult_list)

copy = ult_list[:] or ult_list.copy()
print(copy)

ult_list.insert(5, 'Python')
ult_list.insert(6, 'SQL')
print(ult_list)



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

it_companies.reverse()
print(it_companies)

firstthree = it_companies[:3]
print(firstthree)

lastthree = it_companies[-3:]
print(lastthree)

"""3 isolates the first 3, while -2 takes off the last two"""
"""putting negative in front isolates"""

whoknows = it_companies[3:]
print(whoknows)

mid = it_companies[:middle]



del it_companies[:1]
print(it_companies)

del it_companies[-1:]
print(it_companies)

del it_companies[:]
print(it_companies)
"""deleting the entire list leaves [], not sure if that's supposed to happen"""

del it_companies
"""answer lol"""
