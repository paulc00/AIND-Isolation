from game_agent import MinimaxPlayer
from sample_players import GreedyPlayer
from isolation import isolation


player1 = MinimaxPlayer()
player2 = GreedyPlayer()
game = isolation.Board(player1, player2)

game.apply_move((5, 3))
game.apply_move((0, 0))

player1.time_left = lambda: 99

player1.minimax(game, 4)
