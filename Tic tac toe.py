def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Dikey kazanan kontrolü
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Yatay kazanan kontrolü
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            return board[row][0]

    # Çapraz kazanan kontrolü
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Beraberlik kontrolü
    is_full = all(board[row][col] != " " for row in range(3) for col in range(3))
    if is_full:
        return "Berabere"

    return None

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print("Sıra:", current_player)

        row = int(input("Satırı seçin (0-2): "))
        col = int(input("Sütunu seçin (0-2): "))

        if board[row][col] != " ":
            print("Geçersiz hamle. Lütfen boş bir hücre seçin.")
            continue

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print("Kazanan:", winner)
            break

        current_player = "O" if current_player == "X" else "X"

play_game()

