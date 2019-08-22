import pygame
import sys
import ScreenManager
import PiecePlacer
import GameManager


def main():
    pygame.init()
    pygame.font.init()
    ScreenManager.create_screen()
    board_in_play = GameManager.create_new_board()
    ScreenManager.draw_board()

    move = 0

    while(True):
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                PiecePlacer.place_piece(pygame.mouse.get_pos(), move)
                move += 1


if __name__ == "__main__":
    main()

