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
                polished_coords = PiecePlacer.polish_coordinates(pygame.mouse.get_pos())
                if PiecePlacer.is_valid_coordinate(polished_coords):
                    board_coord = PiecePlacer.from_x_y_to_board_coord(polished_coords)
                    board_in_play = PiecePlacer.place_piece(board_coord, board_in_play, move)
                    move += 1
                    print(board_in_play)
                else:
                    pass


if __name__ == "__main__":
    main()

