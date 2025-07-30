class Card:  # inherits from 'object'
    def __init__(self, rank, suit):
        # self.NAME = VALUE
        self._rank = rank  # "private"
        self._suit = suit

    @property  # decorator
    def rank(self):  # getter property
        return self._rank
    # rank = property(rank)  returns a 'property' object

    @rank.setter
    def rank(self, value):
        if isinstance(value, str):
            self._rank = str
        else:
            raise TypeError("rank must be a string")

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        if isinstance(value, str):
            self._suit = str
        else:
            raise TypeError("suit must be a string")

    def __str__(self):
        return f"Card:{self.rank}/{self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card('8', 'Diamonds')
    c2 = Card('A', 'Hearts')
    print(c1)  # str()
    print(f"{c1 = }")  # repr()
    print(f"{c1.rank = }")  # naughty!!
    print(f"{c1.suit = }")
    c1.rank = "J"

