def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
            col = int(
                input(f"Player {current_player}, enter column (1-3): ")) - 1

            if board[row][col] == ' ':
                board[row][col] = current_player
            else:
                print("Cell already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    tic_tac_toe()
