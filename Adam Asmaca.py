import random

# Kelimeler listesi
words = ["python", "programlama", "odev", "merhaba", "oyun", "NFT","minecraft", "bitcoin", "kelime", "yapay zeka", "defter"]

def select_word():
    return random.choice(words)

def play_game():
    word = select_word()
    guessed_letters = []
    tries = 6

    print("Adam Asmaca Oyununa Hoş Geldiniz!")
    print("Tahmin etmeniz gereken kelime {} harf içeriyor.".format(len(word)))

    while tries > 0:
        print("\nTahmin edilen harfler:", " ".join(guessed_letters))

        # Kalan can sayısı ve adam asmaca resmi
        print("Kalan can: ", tries)
        draw_hangman(tries)

        guess = input("Bir harf tahmin edin: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("Bu harfi zaten tahmin ettiniz. Başka bir harf deneyin.")
            elif guess in word:
                print("Doğru tahmin!")
                guessed_letters.append(guess)
                if all(letter in guessed_letters for letter in word):
                    print("Tebrikler! Kelimeyi doğru tahmin ettiniz:", word)
                    break
            else:
                print("Yanlış tahmin!")
                tries -= 1
        else:
            print("Geçersiz giriş. Lütfen tek bir harf girin.")

    if tries == 0:
        print("Oyunu kaybettiniz! Doğru kelime:", word)

def draw_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    print(stages[tries])

play_game()
