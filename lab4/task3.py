
class Worker:
    def __init__(self, first_name: str, last_name: str, income_per_hour: float):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.income_per_hour: float = income_per_hour
        self.__worked_hours: int = 0
        self.salary: float = 0

    def work(self, duration: int):
        self.__worked_hours += duration
        self.salary = self.salary + self.income_per_hour * duration

    def introduction(self) -> str:
        return f'My name is {self.first_name} {self.last_name}. I have worked for {self.__worked_hours} in this company. Since my last salary I earned myself {self.__salary}!'

    def salary(self):
        print(f'You got {self.salary}$')
        self.salary = 0


class Monster:
    def __init__(self, name: str, max_health: float, damage: int):
        self.name: str = name
        self.max_health: float = max_health
        self.health: float = max_health
        self.damage: int = damage

    def attack_worker(self, worker):
        worker.salary -= self.damage

    def heal(self, amount: int):
        self.health = min(self.health + amount, self.max_health)

    def summary(self) -> str:
        return f"""Monster name: {self.name}
        Health: {self.health}/{self.max_health}
        Damage: {self.damage}"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Compartment:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.contents = []


class Fridge:
    def __init__(self, manufacturer, capacity):
        self.manufacturer = manufacturer
        self.cooling_compartment = Compartment("Cooling", capacity)
        self.freezing_compartment = Compartment("Freezing", capacity)

    def add_product_to_cooling(self, name, price):
        product = Product(name, price)
        self.cooling_compartment.contents.append(product)

    def add_product_to_freezing(self, name, price):
        product = Product(name, price)
        self.freezing_compartment.contents.append(product)

    def show_cooling_compartment_contents(self):
        print("Cooling Compartment Contents:")
        for product in self.cooling_compartment.contents:
            print(f"- {product.name}: ${product.price}")

    def show_freezing_compartment_contents(self):
        print("Freezing Compartment Contents:")
        for product in self.freezing_compartment.contents:
            print(f"- {product.name}: ${product.price}")