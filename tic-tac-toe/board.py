from enums import Player

class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        print("-" * 9)
        for row in self.grid:
            print(" | ".join(row))
            print("-" * 9)

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.grid[row][col] == " "

    def make_move(self, row, col, player: Player):
        if self.is_valid_move(row, col):
            self.grid[row][col] = player.value
            return True
        return False

    def check_winner(self):
        lines = []

        # rows and cols
        for i in range(3):
            lines.append(self.grid[i])  # rows
            lines.append([self.grid[j][i] for j in range(3)])  # columns

        # diagonals
        lines.append([self.grid[i][i] for i in range(3)])
        lines.append([self.grid[i][2 - i] for i in range(3)])

        for line in lines:
            if line.count(line[0]) == 3 and line[0] != " ":
                return line[0]  # Return winning symbol

        return None

    def is_full(self):
        return all(cell != " " for row in self.grid for cell in row)
