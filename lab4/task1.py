import math

class Triangle:
    def __init__(self, base, side):
        self.__name: str = 'Triangle'
        self.base: float = base
        self.side: float = side

    # Task description said that when we calculate circuit we assume it is equilateral triangle
    # not sure if it applies to area but let's say it does
    def area(self) -> float:
        height = math.sqrt(self.side ** 2 - (1 / 4) * self.base ** 2)
        return 0.5 * self.base * height

    def circuit(self) -> float:
        return self.side * 2 + self.base

    def introduction(self) -> str:
        return f"Hi, I'm {self.__name}. lol"


class Rectangle:
    def __init__(self, a, b):
        self.__name: str = 'Rectangle'
        self.a: float = a
        self.b: float = b

    def area(self) -> float:
        return self.a * self.b

    def circuit(self):
        return 2 * self.a + 2 * self.b

    def introduction(self) -> str:
        return f"Hi, I'm {self.__name}. xD"


class Circle:
    def __init__(self, r):
        self.__name: str = 'Circle'
        self.r: float = r

    def area(self) -> float:
        return math.pi * self.r ** 2

    def circuit(self):
        return 2 * math.pi * self.r

    def introduction(self) -> str:
        return f"Hi, I'm {self.__name}. ○"
