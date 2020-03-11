import random
import copy

from sudokuSolver.DoublePoint import DoublePoint
from sudokuSolver.Point import Point

class SudokuOperationProvider:
    sudokuArrLenght = 9
    sudokuGrid = []
    solvedSudokuGrid = []
    coordinatesRangeInEachStep = []
    difficultyRangeValue = [Point(50, 60), Point(36, 49), Point(32, 35), Point(28, 31), Point(22, 27)]

    def __init__(self):
        self._prepareCoordinatesLimits()
        self._prepareGrid()

    def _prepareGrid(self):
        column = []
        appendedValueToCell = 0
        for i in range(0, self.sudokuArrLenght):
            for j in range(0, self.sudokuArrLenght):
                column.append(appendedValueToCell)
            self.sudokuGrid.append(column)
            self.solvedSudokuGrid.append(column)
            column = []

    def _prepareCoordinatesLimits(self):
        x1 = [0, 0, 0, 3, 3, 3, 6, 6, 6]
        y1 = [2, 2, 2, 5, 5, 5, 8, 8, 8]
        x2 = [0, 3, 6, 0, 3, 6, 0, 3, 6]
        y2 = [2, 5, 8, 2, 5, 8, 2, 5, 8]
        for i in range(0, self.sudokuArrLenght):
            self.coordinatesRangeInEachStep.append(DoublePoint(Point(x1[i], y1[i]), Point(x2[i], y2[i])))

    def isPossible(self, col, row, number):
        return self._isColumnAndRowPossible(col, row, number) \
               and self._isCellLocationPossible(col, row, number)


    def _isColumnAndRowPossible(self, col, row, number):
        for i in range(0, self.sudokuArrLenght):
            if self.sudokuGrid[col][i] == number:
                return False
            if self.sudokuGrid[i][row] == number:
                return False
        return True

    def _isCellLocationPossible(self, col, row, number):
        foundedCell = self._findTheCell(col, row) - 1
        corX1Barier = self.coordinatesRangeInEachStep[foundedCell].getPointX1()
        corY1Barrir = self.coordinatesRangeInEachStep[foundedCell].getPointY1()
        corX2Barier = self.coordinatesRangeInEachStep[foundedCell].getPointX2()
        corY2Barrir = self.coordinatesRangeInEachStep[foundedCell].getPointY2()

        for i in range(corX1Barier, corY1Barrir + 1):
            for j in range(corX2Barier, corY2Barrir + 1):
                if self.sudokuGrid[i][j] == number:
                    return False
        return True

    def _findTheCell(self, corX, corY):
        for i in range(0, self.sudokuArrLenght):
            corX1Barier = self.coordinatesRangeInEachStep[i].getPointX1()
            corY1Barrir = self.coordinatesRangeInEachStep[i].getPointY1()
            corX2Barier = self.coordinatesRangeInEachStep[i].getPointX2()
            corY2Barrir = self.coordinatesRangeInEachStep[i].getPointY2()

            if corX1Barier <= corX <= corY1Barrir \
                    and corX2Barier <= corY <= corY2Barrir:
                return i + 1

    def _solve(self):
        for i in range(self.sudokuArrLenght):
            for j in range(self.sudokuArrLenght):
                if self.sudokuGrid[i][j] == 0:
                    for n in range(1, 10):
                        if self.isPossible(i, j, n):
                            self.sudokuGrid[i][j] = n
                            self._solve()
                            if not self.isSudocuSolved():
                                self.sudokuGrid[i][j] = 0
                    return

    def _generateSolvedSudoku(self, randomCounter, includedColumnsForRndGen):
        isSolve = False
        while isSolve != True:
            counter = 0
            currentNumber = 1
            while counter != randomCounter:
                randPositionX = random.randint(0, includedColumnsForRndGen)
                randPositionY = random.randint(0, self.sudokuArrLenght - 1)
                if self.isPossible(randPositionX, randPositionY, currentNumber):
                    self.sudokuGrid[randPositionX][randPositionY] = currentNumber
                currentNumber += 1
                if currentNumber == 10:
                    currentNumber = 1
                counter += 1
            self._solve()
            if self.isSudocuSolved():
                isSolve = True

    def isSudocuSolved(self):
        for i in range(0, self.sudokuArrLenght):
            for j in range(0, self.sudokuArrLenght):
                if self.sudokuGrid[i][j] == 0:
                    return False
        return True

    def printSudoku(self):
        for row in self.sudokuGrid:
            print(' '.join(map(str, row)))

    def printSolvedSudoku(self):
        for row in self.solvedSudokuGrid:
            print(' '.join(map(str, row)))

    def getSudokuGrid(self):
        return self.sudokuGrid

    def getSudokuGridDeepCopy(self):
        return copy.deepcopy(self.sudokuGrid)

    def getSolvedSudokuGrid(self):
        return self.solvedSudokuGrid

    def getSolvedSudokuGridDeepCopy(self):
        return copy.deepcopy(self.solvedSudokuGrid)

    def generateSudoku(self, difficultyScale, randomCounter, includedColumnsForRndGen):

        self._setCellsToZero()
        self._generateSolvedSudoku(randomCounter, includedColumnsForRndGen)
        self.solvedSudokuGrid = self.getSudokuGridDeepCopy()
        difficultyNum = pow(self.sudokuArrLenght, 2) - self._loadAndComputeDiffucultyByChoice(difficultyScale)
        counter = difficultyNum
        i = 0
        while counter != 0:
            corX1Barier = self.coordinatesRangeInEachStep[i].getPointX1()
            corY1Barrir = self.coordinatesRangeInEachStep[i].getPointY1()
            corX2Barier = self.coordinatesRangeInEachStep[i].getPointX2()
            corY2Barrir = self.coordinatesRangeInEachStep[i].getPointY2()
            rndCorX = random.randint(corX1Barier, corY1Barrir)
            rndCorY = random.randint(corX2Barier, corY2Barrir)
            if self.sudokuGrid[rndCorX][rndCorY] == 0:
                continue
            self.sudokuGrid[rndCorX][rndCorY] = 0
            i += 1
            if i == self.sudokuArrLenght:
                i = 0
            counter -= 1
        return

    def checkIfSolved(self):
        for i in range(0, self.sudokuArrLenght):
            for j in range(0, self.sudokuArrLenght):
                if self.sudokuGrid[i][j] != self.solvedSudokuGrid[i][j]:
                    return False
        return True

    def checkIfSolved(self, sudokuGrid):
        for i in range(0, self.sudokuArrLenght):
            for j in range(0, self.sudokuArrLenght):
                if sudokuGrid[i][j] != self.solvedSudokuGrid[i][j]:
                    return False
        return True



    def _loadAndComputeDiffucultyByChoice(self, difficultyScale):
        limitMin = self.difficultyRangeValue[difficultyScale.value - 1].getPointX1()
        limitMax = self.difficultyRangeValue[difficultyScale.value - 1].getPointX2()
        return random.randint(limitMin, limitMax)

    def _setCellsToZero(self):
        for i in range(0, self.sudokuArrLenght):
            for j in range(0, self.sudokuArrLenght):
                self.sudokuGrid[i][j] = 0
                self.solvedSudokuGrid[i][j] = 0
