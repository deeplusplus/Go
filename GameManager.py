from OccupationEnum import Occupation
from typing import Tuple, List


def create_new_board() -> List[Tuple[str, Occupation]]:
    board_points = []
    for character_unicode in range(65, 85):
        board_point_x = chr(character_unicode)
        for index in range(1, 20):
            board_point_y = index
            board_point = str(board_point_x + str(board_point_y))
            board_points.append((board_point, Occupation.Empty))
    return board_points
