from sudokuSolver.SudokuOperationProvider import SudokuOperationProvider
from sudokuSolver.SudokuDifficultyEnum import SudokuDifficultyEnum

from graphics import *

from sudokuVisualController.Button import Button


def main():
    sudoku = SudokuOperationProvider()
    sudoku.generateSudoku(SudokuDifficultyEnum.pathetic, 100, 2)

    gridLenght = 9
    win = GraphWin("Sudoku", 500, 550)
    win.setBackground("azure1")


    btn = Button(win, Point(100, 515), 50, 50, "Exit")
    btn.activate()

    setHorLinesForGrid(win)
    setVerLinesForGrid(win)
    counter = 0
    entryText = []
    for x in range(1, gridLenght + 1):
        for y in range(1, gridLenght + 1):
            if sudoku.getSudokuGrid()[x-1][y-1] != 0:
                message = Text(Point(y * 50, x * 50), sudoku.getSudokuGrid()[x-1][y-1])
                message.draw(win)
            else:
                entryText.append(Entry(Point(y * 50, x * 50), 1))
                entryText[counter].draw(win)
                counter += 1

    while True:
        clickPoint = win.getMouse()
        if btn.clicked(clickPoint):
            fillSudokuFromInput(sudoku, entryText)
            if sudoku.checkIfSolved():
                win.setBackground("Green")
            else:
                win.setBackground("Red")

    win.getMouse()
    win.close()


def fillSudokuFromInput(sudoku, entryPoint):
    counter = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku.getSudokuGrid()[i][j] == 0:
                cislo = entryPoint[counter].getText()
                sudoku.getSudokuGrid()[i][j] = int(entryPoint[counter].getText())
                counter += 1




def setHorLinesForGrid(win):
    line1Hor = Line(Point(30, 25), Point(468, 25))
    line2Hor = Line(Point(30, 175), Point(468, 175))
    line3Hor = Line(Point(30, 325), Point(468, 325))
    line4Hor = Line(Point(30, 475), Point(468, 475))
    line5Hor = Line(Point(30, 75), Point(468, 75))
    line6Hor = Line(Point(30, 125), Point(468, 125))
    line7Hor = Line(Point(30, 225), Point(468, 225))
    line8Hor = Line(Point(30, 275), Point(468, 275))
    line9Hor = Line(Point(30, 375), Point(468, 375))
    line10Hor = Line(Point(30, 425), Point(468, 425))

    line1Hor.setWidth(5)
    line2Hor.setWidth(5)
    line3Hor.setWidth(5)
    line4Hor.setWidth(5)
    line5Hor.setWidth(3)
    line6Hor.setWidth(3)
    line7Hor.setWidth(3)
    line8Hor.setWidth(3)
    line9Hor.setWidth(3)
    line10Hor.setWidth(3)

    line1Hor.draw(win)
    line2Hor.draw(win)
    line3Hor.draw(win)
    line4Hor.draw(win)
    line5Hor.draw(win)
    line6Hor.draw(win)
    line7Hor.draw(win)
    line8Hor.draw(win)
    line9Hor.draw(win)
    line10Hor.draw(win)

def setVerLinesForGrid(win):
    line1Ver = Line(Point(32, 25), Point(32, 475))
    line2Ver = Line(Point(175, 25), Point(175, 475))
    line3Ver = Line(Point(325, 25), Point(325, 475))
    line4Ver = Line(Point(465, 25), Point(465, 475))
    line5Ver = Line(Point(75, 25), Point(75, 475))
    line6Ver = Line(Point(122, 25), Point(122, 475))
    line7Ver = Line(Point(223, 25), Point(223, 475))
    line8Ver = Line(Point(275, 25), Point(275, 475))
    line9Ver = Line(Point(375, 25), Point(375, 475))
    line10Ver = Line(Point(426, 25), Point(426, 475))

    line1Ver.setWidth(5)
    line2Ver.setWidth(5)
    line3Ver.setWidth(5)
    line4Ver.setWidth(5)
    line5Ver.setWidth(3)
    line6Ver.setWidth(3)
    line7Ver.setWidth(3)
    line8Ver.setWidth(3)
    line9Ver.setWidth(3)
    line10Ver.setWidth(3)

    line1Ver.draw(win)
    line2Ver.draw(win)
    line3Ver.draw(win)
    line4Ver.draw(win)
    line5Ver.draw(win)
    line6Ver.draw(win)
    line7Ver.draw(win)
    line8Ver.draw(win)
    line9Ver.draw(win)
    line10Ver.draw(win)

main()
