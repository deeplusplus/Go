import pygame


def attempt_to_place(piece_to_place_x, piece_to_place_y):
    return True


def _notify_invalid_spot():
    error__red = (139, 0, 0)
    error_background = (132, 132, 130)
    notification_font = pygame.font.SysFont('Arial', 18, False, False, None)
    error_surface = notification_font.render('Invalid piece placement', False, error__red, error_background)
    surface = pygame.display.get_surface()
    surface.blit(error_surface, (300, 300))


def place_piece(mouse_click_pos, move):
    color = (255, 255, 255) if move % 2 == 0 else (0, 0, 0)
    piece_to_place_x = _determine_x_coordinate(mouse_click_pos[0])
    piece_to_place_y = _determine_y_coordinate(mouse_click_pos[1])

    is_valid_spot = attempt_to_place(piece_to_place_x, piece_to_place_y)

    if is_valid_spot:
        pygame.draw.circle(pygame.display.get_surface(), color, (piece_to_place_x, piece_to_place_y), 15)
    else:
        _notify_invalid_spot()


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
