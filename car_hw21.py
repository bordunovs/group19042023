from datetime import datetime

class Car:
    def __init__(self, manufacturer, model, year=2020, mileage=0, fuel_consumption=0.0):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f"Автомобіль {self.manufacturer} {self.model}, {self.year} року випуску"

    @property
    def age(self):
        current_year = datetime.today().year
        return current_year - self.year


car1 = Car("Audi", "A4", 2019, 50000, 8.5)
car2 = Car("BMW", "X5", fuel_consumption=10.2)
car3 = Car("Mercedes-Benz", "E-Class", 2017, 80000)

print(car1)
print(car2)
print(car3)

print(f"Вік автомобіля {car1.manufacturer} {car1.model}: {car1.age} років")
print(f"Вік автомобіля {car2.manufacturer} {car2.model}: {car2.age} років")
print(f"Вік автомобіля {car3.manufacturer} {car3.model}: {car3.age} років")
