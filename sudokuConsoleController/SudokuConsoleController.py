from curses.ascii import isdigit

from sudokuSolver import SudokuSolver
from sudokuSolver import  SudokuDifficultyEnum

# Solution for playing sudoku with console created by Admi
# Select coordinates from 1 to 9 for x and y axis, forexample [9, 9] or [5, 6]
# For harder solution, change:
# First paramether - solution -> change number of filled numbers
# Second paramether - number of random number passages, which randomly add numbers before filling sudoku
# Third paramether - number of columns, to which second paramether will generate numbers
# This two paramether controlls difficulty flow significantlty, but with higher numbers, longer time to generate sudoku
# Difficulty:
# 1 - Pathetic
# 2 - Easy
# 3 - Medium
# 4 - Hard
# 5 - Evil
# All rights reserved


def checkIfdiffSelectCorrectly(diff):
    isCorrect = True
    if not isdigit(diff):
        return False




diff = input("Select difficulty: ")
checkIfdiffSelectCorrectly(diff)

