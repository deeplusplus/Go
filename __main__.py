import pygame
import sys
from Core import ScreenManager, PiecePlacer

def main():
    pygame.init()
    pygame.font.init()
    ScreenManager.create_screen()
    ScreenManager.draw_board()
    move = 0

    while(True):
        pygame.display.update()
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if(event.type == pygame.MOUSEBUTTONDOWN):
                PiecePlacer.place_piece(pygame.mouse.get_pos(), move)
                move += 1


if __name__ == "__main__":
    main()

