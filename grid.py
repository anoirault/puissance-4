import numpy as np

class Grid():
    def __init__(self, nLines:int, nCol:int, maxTurn=10000):

        self.nLines = nLines
        self.nCol = nCol

        self.maxTurn = maxTurn

        self.turn = 0

        self.grid = np.zeros(shape=(nLines, nCol), dtype=np.uint8)
        #                0 1 2 3 4
        self.l_reward = [0,0,1,2,10]

    def __str__(self) -> str:
        string = ""

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                string += str(self.grid[i, j])+" "
            string += "\n"

        return string

    def insert(self, col:int, player:int):

        col -= 1

        maskedGrid = np.copy(self.grid)

        maskedGrid[maskedGrid>0] = 1

        summed = np.sum(maskedGrid[:, col], dtype=np.uint8)

        if (col < 0) or (col > self.nCol):
            print("Invalid column : wrong column index")
            return False

        if(summed>=self.nLines):
            print("Invalid column : the column is full")
            return False
        else:
            self.grid[self.nLines-summed-1, col] = player
            return True
        
    def step(self, col:int, player:int):
        
        turn += 1

        if(self.insert(col, player)):
            reward = 0
        else:
            reward = -10

        _, plusHit = self.winCond(player)

        _, minusHit = self.winCond(player%2+1)

        for _, maxHit, _, _ in plusHit:
            reward += self.l_reward[maxHit]
        for _, maxHit, _, _ in minusHit:
            reward -= self.l_reward[maxHit]

        # _ , maxAlligned, _, _ = self.winCond(player)

        # reward += maxAlligned

        # _ , maxAlligned, _, _ = self.winCond(player%2+1)

        # reward -= maxAlligned

        terminated = self.isFull()

        truncated = turn == self.maxTurn

        return self.grid, reward, terminated, truncated, turn

    def reset(self):

        self.turn = 0

        self.grid = np.zeros(shape=(self.nLines, self.nCol), dtype=np.uint8)

        


    def checkAlign(self, n:int, dir:tuple[int,int], line:int, col:int, maxAlligned:int):
        if ((line + dir[0] >= 0) and (line + dir[0] < self.nLines)) and ((col + dir[1] >= 0) and (col + dir[1] < self.nCol)):
            if(self.grid[line + dir[0], col + dir[1]] == n):
                line = line + dir[0]
                col = col + dir[1]
                _, maxAlligned = self.checkAlign(n, dir, line, col, maxAlligned+1)

        return n, maxAlligned
    
    def winCond(self, playerTurn = None):
        hit = []
        maxHit = (0, 0, (0, 0), (0, 0))

        dir = [(0, 1), (1, 0), (1, 1), (-1, -1)]

        for d in dir:
            for i in range(len(self.grid)):
                for j in range(len(self.grid[0])):
                    if(self.grid[i, j] != 0):
                        n, maxAlligned = self.checkAlign(n=self.grid[i, j], dir=d, line=i, col=j, maxAlligned=1)
                        hit.append((n , maxAlligned, (i, j), d))

                        if not (playerTurn is None):
                            if playerTurn == self.grid[i, j] and maxAlligned > maxHit[1]:

                                maxHit = hit[-1]
                        elif maxAlligned > maxHit[1]:
                            
                            maxHit = hit[-1]
        return maxHit, hit
    
    def isFull(self):
        masked = np.copy(self.grid)
        masked[masked>0]=1

        return np.sum(masked) == self.nCol*self.nLines

if __name__ == "__main__":
    grid  = Grid(6, 7)
    while(grid.insert(1, 1)):
        a = 1
    print(grid)
    print(grid.winCond())