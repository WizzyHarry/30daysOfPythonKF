dog = {'name':'',
       'color':'',
       'breed':'',
       'legs':'',
       'age':''}

student = {'first_name':'',
           'last_name':'',
           'gender':'',
           'age':'',
           'married?':'',
           'skills': ['Hola', 'Hello', 'こにちは'],
           'country':'',
           'city':'',
           'address':''} #im not sure if these are empty
print(len(student))
print(student['first_name'])
#an error I believe was supposed to occur because I didn't do .get
print(student.get('first_name'))

aimingforerror = {'key1':None, 'key2':None, 'key3':None}

print(aimingforerror['key1']) #no error :/

value_skills = student['skills']
print("What is in skills: ", value_skills)
print("Data type is: ", type(value_skills)) #it is a list

student['skills'].append('かわ')
student['skills'].append('River')
print(student['skills'])

keys = list(student.keys())
print(keys)
values = list(student.values())
print(values) 
tupleinstudent = list(student.items())
print(tupleinstudent)
del student['first_name']
del dog
print(student)
print(dog) #produces error now 

