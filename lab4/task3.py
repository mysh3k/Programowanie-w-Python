
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


class Fridge:
    def __init__(self):
        self.insides = []