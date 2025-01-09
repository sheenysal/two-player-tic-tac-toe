def print_board(board):
    """
    Prints the Tic Tac Toe board.
    """
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_win(board, player):
    """
    Checks if the player has won the game.
    """
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                      (0, 4, 8), (2, 4, 6)]  # Diagonal
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def tic_tac_toe():
    """
    Runs the Tic Tac Toe game between two players.
    """
    board = [' ' for _ in range(9)]
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")

    while ' ' in board:
        print_board(board)

        # Player move
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != ' ':
                print("This spot is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid move. Please choose a number between 1 and 9.")
            continue

        # Place the mark
        board[move] = current_player

        # Check for a winner
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

    if ' ' not in board:
        print_board(board)
        print("It's a tie!")


# Run the game
if __name__ == "__main__":
    tic_tac_toe()
