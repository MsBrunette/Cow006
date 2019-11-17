class Card:
    def __init__(self, number):
        self.number = number
        if self.number == 55:
            self.glasses = 7
        elif not (self.number % 11):
            self.glasses = 5
        elif not (self.number % 10):
            self.glasses = 3
        elif not (self.number % 5):
            self.glasses = 2
        else:
            self.glasses = 1

    def __repr__(self):
        return f'card "{self.number}" with glasses {self.glasses}'

    def __lt__(self, other):
        return self.number < other.number

    def __eq__(self, other):
        return self.number == other.number

    def __hash__(self):
        return self.number

    def __sub__(self, other):
        return self.number - other.number


if __name__ == "__main__":
    assert(Card(55).glasses == 7)
    assert(Card(50).glasses == 3)
    assert(Card(5).glasses == 2)
    assert(Card(75).glasses == 2)
    assert(Card(77).glasses == 5)
    assert(Card(101).glasses == 1)
    assert(Card(2).glasses == 1)
    assert(Card(80).glasses == 3)

    assert(Card(50) < Card(79))
    assert(Card(102) > Card(3))

    print(Card(5))
    print(Card(72))
    print(Card(104))
    print(Card(55))
