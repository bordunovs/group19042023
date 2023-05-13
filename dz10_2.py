past_cities = set(input("Введите через пробел города, в которых вы были за прошедшие 10 лет: ").split())
future_cities = set(input("Введите через пробел города, куда вы хотите поехать в следующие 10 лет: ").split())

common_cities = past_cities & future_cities

if common_cities:
    print("По-видимому вам вам очень понравилось в городах:" + ', '.join(common_cities))
else:
    print("Вы открыты к чему-то новому.")
