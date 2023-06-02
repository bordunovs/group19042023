students_surnames = input('Ввести фамилии учеников >>> ').title()
for names in students_surnames:
    student_list = students_surnames.split()
    student_list.sort()
print('Фамилии в аофовитном порядке >>> ',student_list)