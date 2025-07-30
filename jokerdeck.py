from card import Card
from carddeck import CardDeck

class Game:
    def register(self):
        pass

class JokerDeck(CardDeck, Game):
    RANKS =  CardDeck.RANKS + ['X']
    def _make_deck(self):
        super()._make_deck()  # call _make_deck() in parent (base) class
        for joker_num in 1, 2:
            card = Card(f"Joker-{joker_num}", "**JOKER**")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    for i in range(8):
        c = j.draw()
        print(c)
    print(f"{len(j) = }")
    print(f"{j.cards = }")
    j.register()
    # method resolution order
    print(f"{JokerDeck.mro() = }")
    