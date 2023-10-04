board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board_size = 3
def draf_board():
    print('-------------')
    for i in range(board_size):
        print(f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
    print('-------------')
def game_step(index, char):
    if (index > 9 or index < 1 or board[index-1] in ('X', 'O')):
        return False

    board[index-1] = char
    return True
def check_win():
    win = False
    win_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5 ,8),
                       (0, 4 , 8), (2, 4, 6)
    )
    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]]) and ((board[pos[1]] == board[pos[2]])):
            win = board[pos[0]]
    return win
def start_game():
    current_player = 'X'
    step = 1
    draf_board()
    while (step < 10) and (check_win() == False):
        index = input(f'Ходит игрок {current_player}. Введите номер поля (0 - выйти из игры):')
        if index == '0':
            break
        if (game_step(int(index), current_player)):
            print(f'Выполнен ход')
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
            draf_board()
            step += 1
        else:
            print(f'Неверный ход. Повторите попытку')
    print(f'Выиграл: {check_win()}')


print(start_game())