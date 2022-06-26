from enum import Enum
from enum import IntEnum


class Card:
    class Color(Enum):
        BLUE = 0,
        GREEN = 1,
        RED = 2,
        YELLOW = 3,


    class Number(IntEnum):
        ONE = 1,
        TWO = 2,
        THREE = 3,
        FOUR = 4,


    class Shape(Enum):
        CROSS = 0,
        DISK = 1,
        SQUARE = 2,
        TRIANGLE = 3,


    class Joker:
        def __str__(self):
            return "Joker"


    def __init__(self, color, number, shape) -> None:
        self._color = color
        self._number = number
        self._shape = shape


    @property
    def color(self):
        return self._color


    @property
    def number(self):
        return self._number


    @property
    def shape(self):
        return self._shape


    def __str__(self):
        return f"Card({self.color}, {self.number}, {self.shape})"
