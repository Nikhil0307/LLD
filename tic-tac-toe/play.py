from game import Game

def main():
    print("Welcome to Tic-Tac-Toe!")
    p1 = input("Enter Player 1's name (X): ") or "Player 1"
    p2 = input("Enter Player 2's name (O): ") or "Player 2"

    game = Game(p1, p2)
    game.play()

    again = input("Play again? (y/n): ").lower()
    if again == 'y':
        main()

if __name__ == "__main__":
    main()
