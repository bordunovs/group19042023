# написати функцію генератор, яка безкінечно даватиме місяці року (тобто перший запит дає січень, потім лютий, і т.д., після грудня знову січень
def get_months():

    months = [
        'Січень',
        'Лютий',
        'Березень',
        'Квітень',
        'Травень',
        'Червень',
        'Липень',
        'Серпень',
        'Вересень',
        'Жовтень',
        'Листопад',
        'Грудень',

    ]
    while True:

     for month in months:
        yield month


month = get_months()

print(next(month))
print(next(month))
print(next(month))
print(next(month))
print(next(month))
print(next(month))
print(next(month))
print(next(month))
print(next(month))
print(next(month))
print(next(month))
print(next(month))

