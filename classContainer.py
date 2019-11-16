from classCard import Card

class Container:
    def __init__(self):
        self.cards = {}

    def add_card(self, Card):
        self.cards[len(self.cards)] = Card

    def pop_card(self, number=0):
        self.cards.pop(number)

    def get_card(self, number):
        return self.cards[number]

    def __len__(self):
        return len(self.cards)

    # def __repr__(self):
    #     num = 0
    #     for i in self.cards.keys():
    #         num += 1
    #         print(f'{num} : {self.cards[i]}')
    #     return ''

    def __repr__(self):
        for i, it in enumerate(self.cards):
            print(f'{i+1} : {self.cards[it]}')
        return ''


if __name__ == "__main__":
    # class Deck(Container):
    #     def __init__(self, countCards):
    #         super().__init__()
    #         i = 0
    #         while i < countCards:
    #             self.cards[i] = Card(i + 1)
    #             i += 1



    print(Deck(14))
    print(Deck(104).cards)


