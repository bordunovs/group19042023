from abc import ABC, abstractmethod
class Character(ABC):

    def __init__(self, model: str, color: str):
        self.mode = model
        self.arm_power = 30
        self.health = 100
    def attack(self, other):
        other.health -= self.arm_power
    @abstractmethod
    def __str__(self):
        pass


class Tank(Character):

    def __init__(self, model: str, color: str, speed: float):
        self.mode = model
        self.color = color
        self.arm_power = 30
        self.health = 100
        self.speed = speed



    def attack(self, other):
        other.health -= self.arm_power

class Artillery(Character):

    def __init__(self, model: str):
        self.mode = model
        self.arm_power = 30
        self.health = 100

    def attack(self, other):
        other.healt -= self.arm_power
    def __str__(self):
        super().__str__()


tank1 = Tank(model='abrams', color='yellow', speed='55')
# tank2 = Tank('abrams', color='yellow', speed='60')
art = Artillery(model='M777')

tank2.attack(art)
tank2.attack(tank1)

pass

# tank1.attack(tank2)
# tank1.attack(tank2)
# tank1.attack(tank2)
# tank1.attack(tank2)
#
# pass