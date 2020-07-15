import pygame
pygame.font.init()


class Tile:
    txtFnt = pygame.font.SysFont('arial', 30)

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = None
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
        if value != 0:
            self.correct = True
        else:
            self.correct = False

    def draw(self, window):
        mPos = pygame.mouse.get_pos()

        space = self.width / 9
        x = self.col * space
        y = self.row * space
        x2 = x + space
        y2 = y + space

        if (x < mPos[0] < x2) & (y < mPos[1] < y2):
            window.fill((191, 192, 191), (x + 1, y + 1, space - 1, space - 1))
        if self.selected:
            pygame.draw.rect(window, (255, 0, 0), (x + 1, y + 1, space - 1, space - 1), 3)
        if self.value != 0:
            text = self.txtFnt.render(str(self.value), 1, (0, 0, 0))
            window.blit(text, (x + 20, y + 15))
        if self.temp is not None:
            text = self.txtFnt.render(str(self.temp), 1, (250, 237, 39))
            window.blit(text, (x + 5, y + 5))

    def guess_num(self, val):
        self.temp = val

    def set(self, val):
        self.value = val
        self.temp = None
        self.correct = True
