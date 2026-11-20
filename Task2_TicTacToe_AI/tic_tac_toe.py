def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")
    print()


def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score


def computer_move(board):
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = "O"


def play_game():
    board = [" "] * 9

    print("Welcome to Tic-Tac-Toe AI!")
    print("You are X and Computer is O.")
    print("Enter positions from 1 to 9.")

    while True:
        print_board(board)

        try:
            move = int(input("Enter your move (1-9): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move! Try again.")
            continue

        board[move] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("Congratulations! You win!")
            break

        if " " not in board:
            print_board(board)
            print("Game Draw!")
            break

        print("Computer is thinking...")
        computer_move(board)

        if check_winner(board, "O"):
            print_board(board)
            print("Computer wins!")
            break

        if " " not in board:
            print_board(board)
            print("Game Draw!")
            break

    input("\nGame finished! Press Enter to close...")


play_game()
