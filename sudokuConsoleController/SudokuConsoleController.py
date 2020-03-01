from sudokuSolver.SudokuOperationProvider import SudokuOperationProvider
from sudokuSolver.SudokuDifficultyEnum import SudokuDifficultyEnum


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

class SudokuConsoleController:
    sudokuControll = SudokuOperationProvider()
    randomScaler = 100
    randomScalerToColumns = 2
    difficulty = SudokuDifficultyEnum.none

    def startGame(self):
        while True:
            diff = input("Select difficulty: ")
            if not self.checkIfdiffSelectCorrectly(diff):
                continue
            self.sudokuControll.generateSudoku(self.chooseDiffFromNumber(diff), self.randomScaler, self.randomScalerToColumns)
            print()
            isFinished = False
            while isFinished != True:
                self.sudokuControll.printSudoku()
                corCol = int(input("Select column: "))
                corRow = int(input("Select row: "))
                number = int(input("Select number: "))
                if self.sudokuControll.isPossible(corCol-1, corRow-1, number):
                    self.sudokuControll.getSudokuGrid()[corCol-1][corRow-1] = number
                if self.sudokuControll.isSudocuSolved():
                    isFinished = True
                print()
            print("Congratz, you won, wonna play again ?")


        #Kontrola zadanych cisel

    def checkIfdiffSelectCorrectly(self, diff):
        isCorrect = True
        if not diff.isdigit():
            return False
        diff = int(diff)
        if not 1 <= diff <= 5:
            return False
        return True

    def chooseDiffFromNumber(self, diff):
        if diff == '1':
            return SudokuDifficultyEnum.pathetic
        elif diff == '2':
            return SudokuDifficultyEnum.easy
        elif diff == '3':
            return SudokuDifficultyEnum.medium
        elif diff == '4':
            return SudokuDifficultyEnum.hard
        elif diff == '5':
            return SudokuDifficultyEnum.evil

new = SudokuConsoleController()
new.startGame()