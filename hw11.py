from pprint import pprint
student = {
    'Ivan Petrov': {
        'Mail': 'Ivan@gmail.com',
        'Age': 14,
        'Phone number': '+380987771221',
        'Average score': 95.8
    },
    'Zhenya Kurych': {
        'Mail': 'Geka@gmail.com',
        'Age': 16,
        'Phone number': None,
        'Average score': 64.5
    },
    'Masha Kera': {
        'Mail': 'Masha@gmail.com ',
        'Age': 18,
        'Phone Number': '+380986671221',
        'Average score': 80
    },

#new_student = {
    'Elena Golovach':{
    'Mail': 'Golovachlena@gmail.com',
    'Age': 22,
    'Phone number': '+380992225566',
    'Average score': 96.2
    }
}

#new_student['Elena Golovach'] = new_student
top_students = []
for name, info in student.items():
    if info['Average score'] > 90:
        fullname = name.split()
        top_students.append({
            'First name': fullname[0],
            'Last name': fullname[1],
            'Average score': info['Average score']
        })

# Print the list of top students
print("List of top students:")
for students in top_students:
    print(f"{students['First name']} {students['Last name']}: {students['Average score']}")
total_score = 0
num_students = 0
for info in student.values():
    total_score += info['Average score']
    num_students += 1

group_average_score = total_score / num_students
print(f"Group average score: {group_average_score:.2f}")
new_student = {

'Mail': 'Golovachlena@gmail.com',
'Age': 22,
'Phone number': None,
'Average score': 96.2

}

if new_student['Phone number'] is None:
    new_student['Phone number parents'] = '+380998887766'
print('Phone number parents', new_student)






