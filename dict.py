# person = {}
# person = {
#    'name': 'Jon',
#    'hobbies': [
#        'tennis',
#       'darts',
#
#    ],
#   'age': 12,
# }
# print(person)

wish1_list = ['name', 'hobbies', 'age']
wish2_list = ['name', 'iban', 'age', 'addeess']

wish1 = set(wish1_list)
wish2 = set(wish2_list)
person = dict.fromkeys(wish1 | wish2, None)
hobbies = [
    'tennis',
    'darts',

],
person['name'] = 'Jone'

pass
