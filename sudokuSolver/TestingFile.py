from sudokuSolver.SudokuSolver import SudokuOperationProvider
from sudokuSolver.SudokuDifficultyEnum import SudokuDifficultyEnum

sudoku = SudokuOperationProvider()
#sudoku.generateSolvedSudoku(100, 2)
#sudoku.printSudoku()
#sdkSolved = sudoku.getSudokuGridDeepCopy()
#sdkSolved[0][0] = 0
#print(sudoku.checkIfSolved(sdkSolved))

sudoku.generateSudoku(SudokuDifficultyEnum.pathetic, 100, 2)
sudoku.printSudoku()
print()
sudoku.printSolvedSudoku()

