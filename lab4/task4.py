class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name}, age: {self.age} years"


class Bird(Animal):
    def __init__(self, name, age, feather_color, wingspan, can_fly):
        super().__init__(name, age)
        self.feather_color = feather_color
        self.wingspan = wingspan
        self.can_fly = can_fly

    def info(self):
        return f"{super().info()}, feather color: {self.feather_color}, " \
               f"wingspan: {self.wingspan} cm"

    def fly(self):
        return f"{self.name} can fly" if self.can_fly else f"{self.name} can't fly"

    def sing(self):
        return f"{self.name} sings beautifully"


eagle = Bird("Eagle", 5, "brown", 200, True)
canary = Bird("Penguin", 2, "black", 60, False)

print(eagle.info())
print(canary.info())

print(eagle.fly())
print(canary.sing())


class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = 100

    def info(self):
        return f"{self.name}, Level {self.level}, Health: {self.health}"

    def attack(self, target):
        return f"{self.name} attacks {target.name}!"


class Warrior(Character):
    def __init__(self, name, level, weapon):
        super().__init__(name, level)
        self.weapon = weapon
        self.stamina = 100

    def info(self):
        return f"{super().info()}, Weapon: {self.weapon}, Stamina: {self.stamina}"

    def slash_attack(self, target):
        damage = 20
        target.health -= damage
        return f"{self.name} performs a slashing attack on {target.name} with {self.weapon} for {damage} damage!"

    def block(self):
        self.stamina -= 10
        return f"{self.name} blocks with their {self.weapon}!"


player1 = Warrior("Warrior1", 1, "Sword")
enemy1 = Character("Enemy1", 1)

print(player1.info())  # Displays: Warrior1, Level 1, Health: 100, Weapon: Sword, Stamina: 100
print(enemy1.info())   # Displays: Enemy1, Level 1, Health: 100

print(player1.slash_attack(enemy1))
print(player1.block())
print(enemy1.info())
print(player1.info())
