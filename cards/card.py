class Card:
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

