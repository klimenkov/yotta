from cards.deck import Deck
from grid import Grid


def main():
    deck = Deck()

    card = deck.take()
    grid = Grid(card)

    print(grid)




if __name__ == "__main__":
    main()



