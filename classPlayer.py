from classContainer import Container
from classCard import Card
from random import choice

class Player:
    def __init__(self, name="Computer"):
        self.name = name
        self.hand = Container()
        self.heap = Container()
        self.chosenCard = None
        self.countedGlasses = 0

    def __repr__(self):
        if self.hand:
            print(f'Player {self.name} with hand:')
            print(self.hand)
            if self.heap:
                print(f'and with heap:')
                print(self.heap)
        elif self.heap:
            print(f'Player {self.name} with heap:')
            print(self.heap)
        else:
            print(f"Player {self.name} doesn't have any cards!")
        return ''

    def choose_card(self):
        self.chosenCard = choice(self.hand.cards)
        for i in self.hand.cards.keys():
            if self.chosenCard == self.hand.cards[i]:
                self.hand.pop_card(i)
                return

    def draw_heap(self, row):
        for i in row.cards.keys():
            self.heap.add_card(row.cards[i])
        self.count_glasses()

    def count_glasses(self):
        self.countedGlasses = 0
        for i in self.heap.cards.keys():
            self.countedGlasses += self.heap.cards[i].glasses

    def score(self):
        return f"Player {self.name} collected {self.countedGlasses} glasses!"

if __name__ == "__main__":
    trus = Player("Coward")

    trus.hand.add_card(Card(5))
    trus.hand.add_card(Card(72))
    trus.hand.add_card(Card(104))

    trus.heap.add_card(Card(55))
    trus.draw_heap(trus.hand)

    cards = {0: Card(5), 1: Card(72), 2: Card(104)}
    cards2 = {0: Card(55), 1: Card(5), 2: Card(72), 3: Card(104)}
    assert(cards == trus.hand.cards)
    assert(cards2 == trus.heap.cards)


    print(trus.hand)
    trus.choose_card()
    print(trus.chosenCard)
    print(trus)
    print(trus.countedGlasses)
    print(trus.score())