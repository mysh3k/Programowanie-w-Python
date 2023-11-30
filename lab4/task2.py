
class Turtle:
    def __init__(self, name, speed):
        self.name: str = name
        self.speed: float = speed   # is speed even needed for this example?
        self.__x: int = 0

    def say_name(self) -> str:
        return f'My name is {self.name}'

    def move(self, distance: int):
        self.__x = self.__x + distance

    def get_position(self) -> str:
        return f'My position is: {self.__x}'
