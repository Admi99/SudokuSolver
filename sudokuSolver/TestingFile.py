from sudokuSolver.SudokuOperationProvider import SudokuOperationProvider
from sudokuSolver.SudokuDifficultyEnum import SudokuDifficultyEnum

sudoku = SudokuOperationProvider()
#sudoku.generateSolvedSudoku(100, 2)
#sudoku.printSudoku()
#sdkSolved = sudoku.getSudokuGridDeepCopy()
#sdkSolved[0][0] = 0
#print(sudoku.checkIfSolved(sdkSolved))


sudoku.generateSudoku(SudokuDifficultyEnum.pathetic, 100, 2)
sdk = sudoku.getSolvedSudokuGridDeepCopy()
sudoku.generateSudoku(SudokuDifficultyEnum.pathetic, 101, 2)

print("No")
def isEqual(sdk):
    for i in range(0, 9):
        for j in range(0, 9):
            if sdk[i][j] != sudoku.getSolvedSudokuGrid()[i][j]:
                return False
    return True


print("No")
counter = 0
while isEqual(sdk) != True:
    counter += 1
    print("Porad jedu")
    sudoku.generateSudoku(SudokuDifficultyEnum.pathetic, 100, 2)

print("Nasel jsem ho")




