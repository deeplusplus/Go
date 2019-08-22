import pygame
from OccupationEnum import Occupation
from typing import Tuple, Dict


def polish_coordinates(mouse_click_pos) -> Tuple[int, int]:
    polished_x = _determine_x_coordinate(mouse_click_pos[0])
    polished_y = _determine_y_coordinate(mouse_click_pos[1])
    return polished_x, polished_y


def is_valid_coordinate(piece_to_place_coords) -> bool:
    piece_to_place_x = piece_to_place_coords[0]
    piece_to_place_y = piece_to_place_coords[1]

    if piece_to_place_x < 30 or piece_to_place_x > 570 or piece_to_place_y < 30 or piece_to_place_y > 570:
        return False
    return True


def _notify_invalid_spot():
    error__red = (139, 0, 0)
    error_background = (132, 132, 130)
    notification_font = pygame.font.SysFont('Arial', 18, False, False, None)
    error_surface = notification_font.render('Invalid piece placement', False, error__red, error_background)
    surface = pygame.display.get_surface()
    surface.blit(error_surface, (300, 300))


def place_piece(board_coord: str, board: Dict[str, int], move: int) -> Dict[str, Occupation]:
    if board[board_coord] is not Occupation.Empty:
        return board

    if move % 2 == 0:
        board[board_coord] = Occupation.White
    else:
        board[board_coord] = Occupation.Black
    return board


def _determine_x_coordinate(initial_x):
    input_remainder = initial_x % 30
    if input_remainder >= 15:
        return initial_x + (30 - input_remainder)
    else:
        return initial_x - input_remainder


def _determine_y_coordinate(initial_y):
    input_remainder = initial_y % 30
    if input_remainder >= 15:
        return initial_y + (30 - input_remainder)
    else:
        return initial_y - input_remainder


def from_x_y_to_board_coord(coordinate: Tuple[int, int]) -> str:
    coord_x = coordinate[0]
    coord_y = coordinate[1]

    board_horizontal = chr(int((coord_x / 30) + 64))
    board_vertical = int(coord_y / 30)

    return board_horizontal + str(board_vertical)
