from .card import Card

from collections import deque
from random import shuffle


class Deck:
    def __init__(self) -> None:
        self._deck = deque(
            Card(color, number, shape)
            for color in Card.Color
            for number in Card.Number
            for shape in Card.Shape)
        self._deck.extend((Card.Joker(), Card.Joker()))

        shuffle(self._deck)


    def take(self):
        return self._deck.pop()


    def put(self, card: Card):
        self._deck.appendleft(card)


    def __str__(self):
        return "\n".join(map(str, self._deck))

