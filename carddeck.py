import random
from card import Card

class CardDeck:
    # class data
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)
    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return f"CardDeck:{len(self)}"

    def __repr__(self):
        return f"CardDeck()"

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    d1.shuffle()
    print(f"{d1.cards = }")
    for _ in range(5):
        c = d1.draw()
        print(c)
    print(f"{len(d1) = }")  # d1.__len__(...)
    print(d1)
    print(f"{d1 = }")
    