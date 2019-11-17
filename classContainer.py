from classCard import Card
from random import shuffle


class Container:
    def __init__(self):
        self.__cards = []

    def add_card(self, Card):
        self.__cards.append(Card)

    def pop_card(self, number=0):
        return self.__cards.pop(number)

    def get_card(self, number):
        return self.__cards[number]

    def __len__(self):
        return len(self.__cards)

    def __repr__(self):
        for i, elem in enumerate(self.__cards):
            print(f'{i + 1} : {elem}')
        return ''

    def shuffle_cards(self):
        shuffle(self.__cards)

    def count_glasses(self):
        # summ = 0
        # for card in self.__cards:
        #     summ += card.glasses
        # return summ
        return sum([x.glasses for x in self.__cards])


if __name__ == "__main__":
    c = Container()
    for i in range(104):
        c.add_card(Card(i + 1))
    print(c)
    print(len(c))
