import random
import numpy
import numpy as np

from player import Player
from grid import Grid

class NPC(Player):
    def __init__(self, n, color=None):
        super().__init__(n, color)


    def chooseColumnSimple(self, grid:Grid, noise = 1):

        p = random.uniform(0,1)

        if(p < noise):
            
            (n, maxAlligned, (i,j), d), hit = grid.winCond(self.number)

            maskedGrid = np.copy(grid.grid)

            maskedGrid[maskedGrid>0] = 1

            summed = np.sum(maskedGrid[:, j], dtype=np.uint8)

            if maxAlligned >= 1:
                return int(random.uniform(1, grid.nCol+1))
            else:
                if((d == (1, 0)) and (np.sum(maskedGrid[:, j], dtype=np.uint8)<Grid.nLines)):
                    return j+1
                
                elif((d == (-1, -1)) and j+1<grid.nCol and (np.sum(maskedGrid[:, min(j+1, grid.nLines-1)], dtype=np.uint8)<grid.nLines)):
                    return j+2
                elif((d == (-1, -1)) and j-maxAlligned > 0 and (np.sum(maskedGrid[:, max(j-maxAlligned, 0)], dtype=np.uint8)<grid.nLines)):
                    return j-maxAlligned+1
                
                elif(j+maxAlligned < grid.nCol and (np.sum(maskedGrid[:, min(j+maxAlligned, grid.nLines-1)], dtype=np.uint8)<grid.nLines)):
                    return j+maxAlligned+1
                elif(j-1 > 0 and (np.sum(maskedGrid[:, max(j-1, 0)], dtype=np.uint8)<grid.nLines)):
                    return j

        return int(random.uniform(1, grid.nCol+1))
    
    def chooseColumnHarder(self, grid: Grid, noise=1):
        
        p = random.uniform(0,1)

        maskedGrid = np.copy(grid.grid)

        maskedGrid[maskedGrid>0] = 1

        if(p < noise):
            (n, maxAlligned, (i,j), d), hit = grid.winCond(1)
            if maxAlligned >= 2:
                if((d == (1, 0)) and (np.sum(maskedGrid[:, j], dtype=np.uint8)<grid.nLines)):
                    return j+1
                
                elif((d == (-1, -1)) and j+1<grid.nCol and (np.sum(maskedGrid[:, min(j+1, grid.nLines-1)], dtype=np.uint8)<grid.nLines)):
                    return j+2
                elif((d == (-1, -1)) and j-maxAlligned > 0 and (np.sum(maskedGrid[:, max(j-maxAlligned, 0)], dtype=np.uint8)<grid.nLines)):
                    return j-maxAlligned+1
                
                elif(j+maxAlligned < grid.nCol and (np.sum(maskedGrid[:, min(j+maxAlligned, grid.nLines-1)], dtype=np.uint8)<grid.nLines)):
                    return j+maxAlligned+1
                elif(j-1 > 0 and (np.sum(maskedGrid[:, max(j-1, 0)], dtype=np.uint8)<grid.nLines)):
                    return j
        
        return self.chooseColumnSimple(grid, noise)