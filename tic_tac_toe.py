def create_game_board(n):
    """creates a n rows and by n column size board"""
    game_board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append('_')

        game_board.append(row)

    return game_board


def display_game_board(game_board):
    for row in range(len(game_board)):
        print(game_board[row])

    print("\n\n")


def take_user_input():
    location = int(input("Enter position you want:"))
    return location


def column(game_board, col):
    return [row[col] for row in game_board]


def winner(game_board, pattern):

    n = len(game_board)
    downward_diagonal = []
    upward_diagonal = []
    for i in range(n):
        # check row or column match
        if game_board[i] == pattern or column(game_board, i) == pattern:
            return True

        for j in range(n):
            if i == j:
                downward_diagonal.append(game_board[i][j])
            if(i + j == n - 1):
                upward_diagonal.append(game_board[i][j])

    if upward_diagonal == pattern or downward_diagonal == pattern:
        return True
    return False


def play_game(game_board, player, position):

    width = len(game_board)
    row = position // width
    col = position % width

    if player == 1:
        game_board[row][col] = 'x'
    else:
        game_board[row][col] = 'o'
    return game_board


def tie(game_board):
    n = len(game_board)
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == '_':
                return False
    return True


def run_game():
    occupied_positions = []
    # create an empty tic-tac-toe game_board
    board_width = 3
    current_player = 1
    pattern1 = ['x' for i in range(board_width)]
    pattern2 = ['o' for i in range(board_width)]

    game_board = create_game_board(board_width)
    # diplay the game board
    display_game_board(game_board)

    pattern = pattern1.copy()

    winner_not_found = True

    while winner_not_found:

        # take input from user
        input_location = take_user_input()

        if (input_location not in occupied_positions):
            occupied_positions.append(input_location)

            # play the game
            game_board = play_game(game_board, current_player, input_location)
            # display the game after one play
            display_game_board(game_board)
            # check winner
            if winner(game_board, pattern):
                print("PLAYER {} WON THE GAME!".format(current_player))
                winner_not_found = False
            else:
                if current_player == 1:
                    current_player = 2
                    pattern.clear()
                    pattern = pattern2.copy()
                else:
                    current_player = 1
                    pattern.clear()
                    pattern = pattern1.copy()

        else:
            # check a tie case
            if tie(game_board):
                print("The Game is a Tie.")
                break
            print("Please enter a new location!")


if __name__ == '__main__':

    run_game()
