# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 23:44:10 2021

@author: Dominik Chodounský
"""

import numpy as np

# class to represent the Sudoku solver along with its methods needed for solving
class SudokuSolver():
    def __init__(self, grid):
        self.grid = grid

    # checks if given number num can be validly placed to coordinates [y,x]
    def is_possible(self, x, y, num):
        # check row and column
        if num in self.grid[:, x] or num in self.grid[y, :]:
            return False
        
        # check smaller 3x3 grid
        x_small = (x // 3) * 3
        y_small = (y // 3) * 3
        if num in self.grid[y_small:y_small + 3, x_small:x_small + 3]:
            return False
        return True
    
    # solves the Sudoku grid using backtracking
    def solve_grid(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    for num in np.arange(1, 10):
                        if self.is_possible(x, y, num):
                            self.grid[y][x] = num
                            self.grid = self.solve_grid()
                            if self.grid is None:
                                return
                            self.grid[y][x] = 0  # backtracking
                    return self.grid
        self.solution = self.grid

if __name__ == '__main__':
    
    grid = np.array([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])
        
    solver = SudokuSolver(grid)
    solver.solve_grid()
    print('Solved SUDOKU:\n')
    print(grid)
    print(' '*10 + '↓')
    print(solver.solution)
    
