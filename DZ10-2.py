students = {
  'Іван Петров': {
    'Пошта': 'Ivan@gmail.com',
    'Вік': 14,
    'Номер телефону': '+380987771221',
    'Середній бал': 95.8
  },
  'Женя Курич': {
    'Пошта': 'Geka@gmail.com',
    'Вік': 16,
    'Номер телефону': None,
    'Середній бал': 64.5
  },
  'Маша Кера': {
    'Пошта': 'Masha@gmail.com',
    'Вік': 18,
    'Номер телефону': '+380986671221',
    'Середній бал': 80
  },
}
print(len(students))
students['Женя Курич']['Вік'] = 25
print(students)