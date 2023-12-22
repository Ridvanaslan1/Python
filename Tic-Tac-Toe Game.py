# Oyun tahtası oluşturma
board = [[" " for _ in range(3)] for _ in range(3)]

# Oyun durumu
current_player = "X"
game_over = False

def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner():
    # Satırları kontrol et
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Sütunları kontrol et
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Çaprazları kontrol et
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def play_game():
    global current_player, game_over

    print("WELCOME TO TİC-TAC-TOE GAME! - BY RIDVAN ASLAN")

    while not game_over:
        print_board()
        row = int(input("Satırı seçin (0-2): "))
        col = int(input("Sütunu seçin (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player

            if check_winner():
                print_board()
                print("Tebrikler! {} oyuncusu kazandı.".format(current_player))
                game_over = True
            elif all(board[i][j] != " " for i in range(3) for j in range(3)):
                print_board()
                print("Oyun berabere bitti.")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Bu hücre zaten dolu. Başka bir hücre seçin.")

play_game()
