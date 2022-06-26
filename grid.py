from cards.card import Card

from typing import List
from typing import Optional
from typing import Tuple


class Grid:
    class Node:
        def __init__(self, index: Tuple[int, int]=(0, 0)) -> None:
            self._index: Tuple[int, int] = index
            self._card_opt: Optional[Card] = None

            self._top_opt: Optional[Grid.Node] = None
            self._right_opt: Optional[Grid.Node] = None
            self._bottom_opt: Optional[Grid.Node] = None
            self._left_opt: Optional[Grid.Node] = None


        def put(self, card: Card) -> bool:
            self._card_opt = card


        def set_hole_top(self):
            i, j = self._index

            self._top_opt = Grid.Node((i-1, j))
            self._top_opt._bottom_opt = self

            return self._top_opt


        def set_hole_right(self):
            i, j = self._index

            self._right_opt = Grid.Node((i, j+1))
            self._right_opt._left_opt = self

            return self._right_opt


        def set_hole_bottom(self):
            i, j = self._index

            self._bottom_opt = Grid.Node((i+1, j))
            self._bottom_opt._top_opt = self

            return self._bottom_opt


        def set_hole_left(self):
            i, j = self._index

            self._left_opt = Grid.Node((i, j-1))
            self._left_opt._right_opt = self

            return self._left_opt


    def __init__(self, card: Card):
        node_initial = Grid.Node()
        node_initial.put(card)

        hole_top = node_initial.set_hole_top()
        hole_right = node_initial.set_hole_right()
        hole_bottom = node_initial.set_hole_bottom()
        hole_left = node_initial.set_hole_left()

        self._holes: List[Grid.Node] = [
            hole_top,
            hole_right,
            hole_bottom,
            hole_left, ]
        



