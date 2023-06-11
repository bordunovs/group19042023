from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, tank_volume, remaining_fuel, speed, mileage):
        self.brand = brand
        self.tank_volume = tank_volume
        self.remaining_fuel = remaining_fuel
        self.speed = speed
        self.mileage = mileage

    @abstractmethod
    def __str__(self):
        pass

    def refuel(self, amount):
        self.remaining_fuel = min(self.remaining_fuel + amount, self.tank_volume)

    def transfer_fuel(self, other_vehicle, amount):
        available_amount = min(amount, self.remaining_fuel, other_vehicle.tank_volume - other_vehicle.remaining_fuel)
        self.remaining_fuel -= available_amount
        other_vehicle.remaining_fuel += available_amount


class Car(Vehicle):
    def __init__(self, brand, tank_volume, remaining_fuel, speed, mileage, passenger_count, airbag_available):
        super().__init__(brand, tank_volume, remaining_fuel, speed, mileage)
        self.passenger_count = passenger_count
        self.airbag_available = airbag_available

    def __str__(self):
        return f"Car: Brand - {self.brand}, Tank Volume - {self.tank_volume}, Remaining Fuel - {self.remaining_fuel}, Speed - {self.speed}, Mileage - {self.mileage}, Passenger Count - {self.passenger_count}, Airbag Available - {self.airbag_available}"


class Motorcycle(Vehicle):
    def __init__(self, brand, tank_volume, remaining_fuel, speed, mileage, cradle_option):
        super().__init__(brand, tank_volume, remaining_fuel, speed, mileage)
        self.cradle_option = cradle_option

    def __str__(self):
        return f"Motorcycle: Brand - {self.brand}, Tank Volume - {self.tank_volume}, Remaining Fuel - {self.remaining_fuel}, Speed - {self.speed}, Mileage - {self.mileage}, Cradle Option - {self.cradle_option}"


car = Car("Toyota", 60, 40, 120, 5000, 4, True)
print(car)

motorcycle = Motorcycle("Honda", 15, 10, 180, 3000, False)
print(motorcycle)

