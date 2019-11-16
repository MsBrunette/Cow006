from classContainer import Container
from classCard import Card
from classPlayer import Player
from random import randint, choice, shuffle

class Game:
    def __init__(self, countCards):
        self.__new_deck__(countCards)
        self.players = {}
        self.tableRows = {}

    def __new_deck__(self, countCards=104):
        self.deck = Container()
        i = 0
        while i < countCards:
            self.deck.cards[i] = Card(i + 1)
            i += 1

    def add_player(self, player=Player()):
        if len(self.players) < 10:
            self.players[len(self.players)] = player

    def start_game(self):
        if len(self.players) < 2:
            self.add_player(Player("Coward"))
            self.add_player(Player("Dipstick"))
            self.add_player(Player("Veteran"))
        shuffle(self.deck.cards)
        self.deal_cards(3, 2)
        #self.choosing_cards()
        #self.add_cards_in_rows()



    def deal_cards(self, countCardsInHands=10, countRowInTable=4):
        d = 0
        for i in range(0,countCardsInHands):
            for y in self.players.keys():
                self.players[y].hand.add_card(self.deck.cards[d])
                #self.deck.pop_card(0)
                d += 1
        for i in range(0, countRowInTable):
            self.tableRows[i] = Container()
            self.tableRows[i].add_card(self.deck.cards[d])
            d += 1

    def choosing_cards(self):
        for i in self.players.keys():
            self.players[i].choose_card()

    def find_row(self, card):
        choosingCardIsMin = False
        difference = {}
        for i in self.tableRows.keys():
            lastCardInRow = self.tableRows[i].cards[len(self.tableRows[i].cards) - 1]
            if lastCardInRow > card:
                choosingCardIsMin = True
                break
            else:
                choosingCardIsMin = False
                difference[i] = card - lastCardInRow
        if choosingCardIsMin:
            return -1
        else:
            findRow = -1
            for i in difference.keys():
                if i == 0:
                    findRow = i
                else:
                    if difference[i] < difference[findRow]:
                        findRow = i
            return findRow

    def add_cards_in_rows(self):
        choosingCards = set()
        for i in self.players.keys():
            choosingCards.add(self.players[i].chosenCard)
        while len(choosingCards) > 0:
            card = min(choosingCards)
            findRow = self.find_row(card)
            if findRow == -1:
                for i in self.players.keys():
                    if self.players[i].chosenCard == card:
                        self.players[i].draw_heap(self.tableRows[0])
                        self.tableRows[0].cards = {}
                        self.tableRows[0].cards[0] = card
            else:
                if len(self.tableRows[findRow].cards) == 5:
                    for i in self.players.keys():
                        if self.players[i].chosenCard == card:
                            self.players[i].draw_heap(self.tableRows[findRow])
                            self.tableRows[findRow].cards = {}
                            self.tableRows[findRow].cards[0] = card
                else:
                    self.tableRows[findRow].add_card(card)
            choosingCards.remove(card)
        for i in self.players.keys():
            self.players[i].chosenCard = None





if __name__ == "__main__":
    game = Game(12)
    game.start_game()
    print(game.players)
    print(game.tableRows)
    game.choosing_cards()
    game.add_cards_in_rows()
    print(game.players)
    print(game.tableRows)