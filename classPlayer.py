from classContainer import Container
from classCard import Card


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
        if len(self.hand) > 1:
            # логика высчитывания выбора карты с руки
            self.chosenCard = self.hand.pop_card(1)
            return True
        else:
            self.chosenCard = self.hand.pop_card()
            return False

    def draw_heap(self, row: Container):
        for _ in range(len(row)):
            self.heap.add_card(row.pop_card())
        self.count_glasses()

    def count_glasses(self):
        self.countedGlasses = self.heap.count_glasses()

    def score(self):
        print(f'Player {self.name} collected {self.countedGlasses} glasses!')


if __name__ == "__main__":
    trus = Player("Coward")

    trus.hand.add_card(Card(5))
    trus.hand.add_card(Card(72))
    trus.hand.add_card(Card(104))
    # trus.choose_card()
    # print(trus.chosenCard)
    trus.heap.add_card(Card(55))
    trus.draw_heap(trus.hand)
    trus.score()
    # cards = {0: Card(5), 1: Card(72), 2: Card(104)}
    # cards2 = {0: Card(55), 1: Card(5), 2: Card(72), 3: Card(104)}
    # assert(cards == trus.hand.__cards)
    # assert(cards2 == trus.heap.__cards)


    # print(trus)
    # print(trus.heap)

    # print(trus)
    print(trus.countedGlasses)
    # print(trus.score())
