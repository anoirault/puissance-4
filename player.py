import numpy as np
from grid import Grid

class Player():
    def __init__(self, n, color):
        self.number = n
        self.color = color

    def chooseColumn(self, grid:Grid):

        col = int(input(f"Choose a column between 1 and {len(grid.grid[0])}\n"))

        while(col > len(grid.grid[0]) or col < 1):
            print("Invalid input")

            col = int(input(f"Choose a column between 1 and {len(grid.grid[0])}\n"))


        return col


if __name__ == "__main__":
    print("PLAYERS")