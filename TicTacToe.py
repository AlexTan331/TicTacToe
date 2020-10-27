import random

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
position = []
players = ['X', 'O']
max_choices = 9


def print_board():
    print('\t1\t 2\t  3\t')
    for i in range(0, len(board)):
        print(f'{i+1}', end=" ")
        print(board[i])


def clear_board():
    for i in range(0, len(board)):
        board[i] = [' ', ' ', ' ']
    position.clear()
    print_board()


def is_replay():
    choice = 'WRONG'

    while choice != 'y' and choice != 'n':
        choice = input("Do you want to replay?(enter Y or N)").lower()

    if choice == 'n':
        return False
    else:
        clear_board()
        return True


def player_choice(current_player):
    validate_row = False
    validate_column = False
    already_picked = True

    while not validate_column or not validate_row or already_picked:
        row = input("Enter the row position in range (1, 2, 3):")
        if not row.isdigit():
            print("Sorry, you did not enter an integer. Please try again")
            continue
        else:
            if int(row) not in range(1, 4):
                print("Sorry, you did not choose a value in the correct range (1, 2, 3)")
                continue
            else:
                validate_row = True

        column = input("Enter the column position in range (1, 2, 3):")
        if not column.isdigit():
            print("Sorry, you did not enter an integer. Please try again")
            continue
        else:
            if int(column) not in range(1, 4):
                print("Sorry, you did not choose a value in the correct range (1, 2, 3)")
                continue
            else:
                validate_column = True

        p = (int(row) - 1, int(column) - 1)
        if p in position:
            print("Sorry, the position you chose has already been picked. Please choose another available position")
            continue
        else:
            position.append(p)
            already_picked = False

    board[position[len(position) - 1][0]][position[len(position) - 1][1]] = current_player
    print_board()


def equals3(a, b, c):
    return a == b and b == c and a != ' '


def check_winner():
    winner = ''

    # check row
    for i in range(0, 3):
        if equals3(board[i][0], board[i][1], board[i][2]):
            winner = board[i][0]
            return winner
    # check column
    for i in range(0, 3):
        if equals3(board[0][i], board[1][i], board[2][i]):
            winner = board[0][i]
            return winner
    # check diagonal
    if equals3(board[0][0], board[1][1], board[2][2]):
        winner = board[0][0]
        return winner
    # check diagonal
    if equals3(board[0][2], board[1][1], board[2][0]):
        winner = board[0][2]
        return winner
    # check tie
    if winner == '' and len(position) == max_choices:
        winner = 'tie'
        return winner

    return winner


def game_on():
    play = True
    print_board()

    while play:
        current_player = players[random.randint(0, 1)]
        while len(position) < max_choices and check_winner() == '':
            player_choice(current_player)
            if current_player == players[0]:
                current_player = players[1]
            elif current_player == players[1]:
                current_player = players[0]

        print(f'result is:{check_winner()}')

        play = is_replay()


game_on()
