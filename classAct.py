from classContainer import Container
from classCard import Card
from classPlayer import Player


class Act:
    def __init__(self, countCards, countCardsInHands, countRowInTable):
        self.deck = Container()
        for i in range(countCards):
            self.deck.add_card(Card(i + 1))
        self.players = []
        self.tableRows = [Container() for _ in range(countRowInTable)]
        self.countCardsInHands = countCardsInHands
        self.playingAct = True

    def add_player(self, playerName):
        if len(self.players) < 10:
            self.players.append(Player(playerName))

    def deal_cards(self, shuffle=True):
        if shuffle:
            self.deck.shuffle_cards()
        for _ in range(self.countCardsInHands):
            for player in self.players:
                player.hand.add_card(self.deck.pop_card())
        for row in self.tableRows:
            row.add_card(self.deck.pop_card())

    def step(self):
        self.choosing_cards()
        self.add_cards_in_rows()

    def choosing_cards(self):
        for player in self.players:
            self.playingAct = player.choose_card()

    def find_row(self, card):
        findRow = None
        found = False
        difference = 0
        for row in self.tableRows:
            diff = card - row.get_card(len(row) - 1)
            if diff > 0 and (difference > diff or difference == 0):
                difference = diff
                findRow = row
                found = True
        if not found:
            minGlasses = 0
            for row in self.tableRows:
                m = row.count_glasses()
                if m < minGlasses or minGlasses == 0:
                    minGlasses = m
                    findRow = row
        return findRow, found

    def add_cards_in_rows(self):
        choosingCards = {}
        for player in self.players:
            choosingCards[player.chosenCard] = player
        while choosingCards:
            card = min(choosingCards)
            findRow, found = self.find_row(card)
            if (found and len(findRow) == 5) or not found:
                choosingCards[card].draw_heap(findRow)
            findRow.add_card(card)
            del choosingCards[card]

    def ending_act(self):
        print('\nResults of act:\n')


if __name__ == "__main__":
    r = Act(10, 2, 2)
    r.add_player("Coward")
    r.add_player("Dipstick")
    r.add_player("Veteran")
    r.deal_cards(shuffle=False)
    r.choosing_cards()
    print('Players: ')
    cards = []
    for pl in r.players:
        print(pl)
        cards.append(pl.chosenCard)
    print('Rows:')
    for row in r.tableRows:
        print(row)
    print(cards)
    card = min(cards)
    print(card)
    print('>>>', r.find_row(card))
    r.add_cards_in_rows()
    print('Rows:')
    for row in r.tableRows:
        print(row)

    print('Players: ')
    cards = []
    for pl in r.players:
        print(pl)
    # print(r.find_row())
    # r.start_game()
    # print(gameRound.players)
    # print(gameRound.tableRows)
    # gameRound.choosing_cards()
    # gameRound.add_cards_in_rows()
    # print(gameRound.players)
    # print(gameRound.tableRows)
