from classGame import Game

game = Game(104, 10, 4)
game.start_game()
while not game.gameOver:
    game.play_act()
