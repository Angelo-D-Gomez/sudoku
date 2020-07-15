import pygame
import sudokuTile
import copy
from sudokuAPIPuzzleGenerator import sudokuBoard
pygame.font.init()


def formatTime(time):
    sec = time%60
    minute = time//60
    if sec < 10:
        formattedTime = str(minute) + ":0" + str(sec)
    else:
        formattedTime = str(minute) + ":" + str(sec)
    return formattedTime


class Grid:
    board = sudokuBoard
    txtFnt = pygame.font.SysFont('arial', 30)

    def __init__(self, rows, columns, width, height, window):
        self.rows = rows
        self.cols = columns
        self.tiles = [[sudokuTile.Tile(self.board[i][j], i, j, width, height) for j in range(self.cols)] for i in
                      range(rows)]
        self.width = width
        self.height = height
        self.window = window
        self.selected = None
        self.solvedPuzzle = copy.deepcopy(self.tiles)
        self.emptyTiles = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.tiles[i][j].value == 0:
                    self.emptyTiles += 1

    def draw(self, guesses, time):
        self.window.fill((255, 255, 255))
        # Draw Grid Lines
        space = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.window, (0, 0, 0), (0, i * space), (self.width, i * space), thickness)
            pygame.draw.line(self.window, (0, 0, 0), (i * space, 0), (i * space, self.height), thickness)

        # Fill in the spaces
        for i in range(self.rows):
            for j in range(self.cols):
                self.tiles[i][j].draw(self.window)

        if guesses <= self.emptyTiles:
            text = self.txtFnt.render(str(guesses), 1, (0, 255, 0))
        else:
            text = self.txtFnt.render(str(guesses), 1, (255, 0, 0))
        if guesses < 10:
            self.window.blit(text, (35, 550))
        elif guesses < 100:
            self.window.blit(text, (20, 550))
        elif guesses >= 100:
            self.window.blit(text, (0, 550))
        text = self.txtFnt.render("/" + str(self.emptyTiles), 1, (0, 0, 0))
        self.window.blit(text, (55, 550))
        formattedTime = formatTime(time)
        text = self.txtFnt.render(formattedTime, 1, (0, 0, 0))
        self.window.blit(text, (455, 550))

    def clicked(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            space = self.width / 9
            x = pos[0] // space
            y = pos[1] // space
            return int(y), int(x)
        else:
            return None

    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.tiles[i][j].selected = False

        self.tiles[row][col].selected = True
        self.selected = (row, col)

    def sketch(self, newValue):
        row, col = self.selected
        if not self.tiles[row][col].correct:
            self.tiles[row][col].guess_num(newValue)

    def guess(self):
        row, col = self.selected
        if self.tiles[row][col].temp == self.solvedPuzzle[row][col].value:
            self.tiles[row][col].set(self.tiles[row][col].temp)
        else:
            self.tiles[row][col].temp = None

    def clear(self):
        row, col = self.selected
        if self.tiles[row][col].value == 0:
            self.tiles[row][col].temp = None

    # solution creation functions found below
    def createSolution(self):
        emptySpot = self.checkEmpty()
        if emptySpot is None:
            return True
        else:
            row, col = emptySpot

        for x in range(1, 10):
            if self.checkValid(row, col, x):
                self.solvedPuzzle[row][col].value = x

                if self.createSolution():
                    return True

                self.solvedPuzzle[row][col].value = 0

        return False

    def checkValid(self, row, col, value):
        for i in range(self.rows):
            if self.solvedPuzzle[i][col].value == value:
                return False

        for i in range(self.cols):
            if self.solvedPuzzle[row][i].value == value:
                return False

        square_y = (row // 3) * 3
        square_x = (col // 3) * 3

        for i in range(square_y, square_y + 3):
            for j in range(square_x, square_x + 3):
                if self.solvedPuzzle[i][j].value == value:
                    return False

        return True

    def checkEmpty(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.solvedPuzzle[i][j].value == 0:
                    return i, j
        return None
    # end of solution creation functions

    def gameOver(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.tiles[i][j].value == 0:
                    return False
        return True
