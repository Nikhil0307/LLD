from enums import Player
from board import Board

class Game:
    def __init__(self, player1_name="Player 1", player2_name="Player 2"):
        self.board = Board()
        self.players = {
            Player.X: player1_name,
            Player.O: player2_name
        }
        self.current_player = Player.X

    def switch_turn(self):
        self.current_player = Player.O if self.current_player == Player.X else Player.X

    def play(self):
        print(f"\nWelcome {self.players[Player.X]} (X) and {self.players[Player.O]} (O)!\n")
        while True:
            self.board.display()
            print(f"{self.players[self.current_player]}'s turn ({self.current_player.value})")

            try:
                move = input("Enter your move as row,col (0-indexed, e.g., 1,2): ")
                row, col = map(int, move.strip().split(","))
            except ValueError:
                print("Invalid input. Format must be row,col (e.g., 1,2)")
                continue

            if not self.board.make_move(row, col, self.current_player):
                print("Invalid move. Try again.")
                continue

            winner = self.board.check_winner()
            if winner:
                self.board.display()
                print(f"\n {self.players[Player(winner)]} ({winner}) wins!")
                break

            if self.board.is_full():
                self.board.display()
                print("\nIt's a draw!")
                break

            self.switch_turn()
