'''
    Dictionaries - Python Key value pairs
    eg: 
        contact_name: contact_number
'''

# student
student = {
    "Name": "Rajaraman",
    "Age": "24",
    "Weight": "90",
    "Marks": "A"
}
print(student)

print(student['Name'])

for x in student:
    print(student[x])


for x, y in student.items():
    print(x, y)

students = {
    'student1': {
        "Name": "Rajaraman",
        "Age": "24",
        "Weight": "90",
        "Marks": "A",
    },
    'student2': {
        "Name": "Rajaraman",
        "Age": "24",
        "Weight": "90",
        "Marks": "A"
    }
}
