from sudokuSolver.SudokuOperationProvider import SudokuOperationProvider
from sudokuSolver.SudokuDifficultyEnum import SudokuDifficultyEnum

from graphics import *

from sudokuVisualController.Button import Button


def main():
    difficulty = [SudokuDifficultyEnum.pathetic,
                  SudokuDifficultyEnum.easy,
                  SudokuDifficultyEnum.medium,
                  SudokuDifficultyEnum.hard,
                  SudokuDifficultyEnum.evil]

    sudoku = SudokuOperationProvider()
    sudoku.generateSudoku(difficulty[0], 100, 2)

    gridLenght = 9
    win = GraphWin("Sudoku", 500, 550)
    win.setBackground("azure1")

    btnCheck = Button(win, Point(67, 515), 70, 40, "Check")
    btnReset = Button(win, Point(150, 515), 70, 40, "Reset")
    btnGen = Button(win, Point(234, 515), 70, 40, "Generate")
    btnDiff = Button(win, Point(323, 515), 80, 40, "Difficulty")
    btnCheck.activate()
    btnReset.activate()
    btnGen.activate()
    btnDiff.activate()

    diffText = Text(Point(415, 515), difficulty[0].name)
    diffText.setStyle("bold")
    diffText.draw(win)


    setHorLinesForGrid(win)
    setVerLinesForGrid(win)
    entryText = []
    labelText = []

    generateGraphics(win, sudoku, entryText,labelText, gridLenght)

    difficultyIndex = 0
    while True:
        sudokuOrigin = sudoku.getSudokuGridDeepCopy()
        clickPoint = win.getMouse()
        if btnCheck.clicked(clickPoint):
            if not fillSudokuFromInput(sudokuOrigin, entryText):
                continue
            if sudoku.checkIfSolved(sudokuOrigin):
                win.setBackground("Green")
            else:
                win.setBackground("Red")
                time.sleep(1)
                win.setBackground("azure1")
        if btnReset.clicked(clickPoint):
            cleareEntryPoints(entryText)
            win.setBackground("azure1")
        if btnGen.clicked(clickPoint):
            sudoku.generateSudoku(difficulty[difficultyIndex], 100, 2)
            clearChangingGraphics(win, labelText, entryText)
            win.setBackground("azure1")
            generateGraphics(win, sudoku, entryText,labelText, gridLenght)
        if btnDiff.clicked(clickPoint):
            if difficultyIndex <= 3:
                difficultyIndex += 1
            else:
                difficultyIndex = 0
            diffText.setText(difficulty[difficultyIndex].name)



    win.getMouse()
    win.close()

def generateGraphics(win, sudoku, entryText,labelText, gridLength):
    counterEntry = 0
    counterLabel = 0
    for x in range(1, gridLength + 1):
        for y in range(1, gridLength + 1):
            if sudoku.getSudokuGrid()[x - 1][y - 1] != 0:
                labelText.append(Text(Point(y * 50, x * 50), sudoku.getSudokuGrid()[x - 1][y - 1]))
                labelText[counterLabel].setTextColor("Blue")
                labelText[counterLabel].setStyle("bold")
                labelText[counterLabel].draw(win)
                counterLabel += 1
            else:
                entryText.append(Entry(Point(y * 50, x * 50), 1))
                entryText[counterEntry].draw(win)
                counterEntry += 1

def clearChangingGraphics(win, labelText, entryText):
    for item in labelText[:]:
        item.undraw()
    for item in entryText[:]:
        item.undraw()
    labelText.clear()
    entryText.clear()
    win.update()

def fillSudokuFromInput(sudoku, entryPoint):
    counter = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] == 0:
                cislo = entryPoint[counter].getText()
                if cislo == "" or not limitNumberEntryCount(cislo, 1):
                    return False
                sudoku[i][j] = int(entryPoint[counter].getText())
                counter += 1
    return True


def limitNumberEntryCount(number, n):
    return len(number) == n;

def cleareEntryPoints(entryPoint):
    for i in range(0, len(entryPoint)):
        entryPoint[i].setText("")

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
    line9Hor.draw(win)
    line8Hor.draw(win)
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

