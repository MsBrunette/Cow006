from functools import reduce

from classContainer import Container
from classCard import Card
from classPlayer import Player
from classAct import Act


class Game:
    def __init__(self, countCards=104, countCardsInHands=10, countRowInTable=4):
        self.countCards = countCards
        self.countCardsInHands = countCardsInHands
        self.countRowInTable = countRowInTable
        self.players = []
        self.winners = []
        self.gameOver = False

    def add_player(self, playerName):
        if len(self.players) < 10:
            self.players.append(Player(playerName))

    def start_game(self):
        if len(self.players) < 2:
            self.add_player("Coward")
            self.add_player("Dipstick")
            self.add_player("Veteran")


    def play_act(self):
        self.act = Act(self.countCards, self.countCardsInHands, self.countRowInTable)
        for player in self.players:
            self.act.add_player(player.name)
        self.act.deal_cards()
        while self.act.playingAct:
            self.act.step()
        self.ending_act()

    def ending_act(self):
        self.act.ending_act()
        for player, act_player in zip(self.players, self.act.players):
            if player.name == act_player.name:
                player.countedGlasses += act_player.countedGlasses
                if player.countedGlasses >= 66:
                    self.gameOver = True
                player.score()

        if self.gameOver:
            self.end_game(self.find_winner())

    def find_winner(self):
        min = 66
        for player in self.players:
            if player.countedGlasses < min:
                min = player.countedGlasses
                self.winners = []
                self.winners.append(player)
            elif player.countedGlasses == min:
                self.winners.append(player)
        if min == 66:
            return False
        else:
            return True

    def end_game(self, findWinner):
        print("\nThe game is over!")
        if findWinner:
            if len(self.winners) > 1:
                winners = []
                for winner in self.winners:
                    winners.append(winner.name)
                print(f'The winners are {winners}')
            else:
                print(f'The winner is {self.winners[0].name}')
        else:
            print(f'Nobody has won...')


if __name__ == "__main__":
    game = Game(10, 2, 2)
