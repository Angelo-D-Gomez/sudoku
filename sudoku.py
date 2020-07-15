import pygame
import sudokuBoard
import time

window = pygame.display.set_mode([540, 600])


def main():
    gameBoard = sudokuBoard.Grid(9, 9, 540, 540, window)
    pygame.display.set_caption("Sudoku")
    run = True
    key = None
    guesses = 0
    gameBoard.createSolution()
    start = time.time()
    final_time = None
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_BACKSPACE:
                    gameBoard.clear()
                    key = None

                if event.key == pygame.K_RETURN:
                    if gameBoard.selected is None:
                        None
                    else:
                        i, j = gameBoard.selected
                        if gameBoard.tiles[i][j].temp is not None:
                            guesses += 1
                            gameBoard.guess()
                        if gameBoard.gameOver():
                            final_time = play_time
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mPos = pygame.mouse.get_pos()
                theClick = gameBoard.clicked(mPos)
                if theClick:
                    gameBoard.select(theClick[0], theClick[1])
                    key = None

        if gameBoard.selected and key is not None:
            gameBoard.sketch(key)
            key = None

        gameBoard.draw(guesses, play_time)
        pygame.display.update()
    while not run:
        gameBoard.draw(guesses, final_time)


main()
