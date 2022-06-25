from .color import Color
from .number import Number
from .shape import Shape

from .card import Card
from .joker import Joker


class Deck:
    def __init__(self) -> None:
        self._deck = {
            Card(color, number, shape)
            for color in Color
            for number in Number
            for shape in Shape } | \
            {Joker(), Joker()}

    def __str__(self):
        return "\n".join(map(str, self._deck))

