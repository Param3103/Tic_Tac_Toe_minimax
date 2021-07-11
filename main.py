from tic_tac_toe import TicTacToe

game = TicTacToe()
while game.is_winner() is None:
    game.display_board()
    if game.is_player_turn() == 'X':
        pos = int(input('player where do you want to play? '))
        game.make_move('X', pos)
    else:
        game.comp_move('O')
game.display_board()
print(game.is_winner())