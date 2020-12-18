def game(player1, player2):
    turn = 1
    game_over = False
    start_board = ('```'
                   ' 1 | 2 | 3 \n'
                   ' - + - + - \n'
                   ' 4 | 5 | 6 \n'
                   ' - + - + - \n'
                   ' 7 | 8 | 9 '
                   '```')

    while not game_over:
        current_board = ''
        if turn == 1:
            current_board = start_board
            print_game(current_board, turn)

        if turn % 2 == 0:
            print('hello player2')
        else:
            print('hello player1')
        board_update(current_board, next_move)
        print(board)


def print_game(current_board, turn):
    print('Turn: ' + turn + '\n\n' + current_board)


def board_update(current_board, next_move):
    new_board = ''
    return new_board


def print_board():
    return ('```   |   |   \n'
            ' - + - + - \n'
            '   |   |   \n'
            ' - + - + - \n'
            '   |   |   \n```')
