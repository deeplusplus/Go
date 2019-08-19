import pygame
import sys


def create_screen():
    window_default_size = (600, 600)
    pygame.display.set_mode(window_default_size, pygame.RESIZABLE)


def draw_board():
    board_color = (255, 192, 66)
    board_draw_info = (10, 10, 590, 590)
    pygame.draw.rect(pygame.display.get_surface(), board_color, board_draw_info)
    _draw_horizontal_lines()
    _draw_vertical_lines()
    _draw_star_points()


def _draw_horizontal_lines():
    black = (0, 0, 0)
    line_points = [[30, 30], [570, 30]]
    surface = pygame.display.get_surface()

    for i in range(0, 19):
        pygame.draw.line(surface, black, line_points[0], line_points[1])
        line_points[0][1] += 30
        line_points[1][1] += 30


def _draw_vertical_lines():
    black = (0, 0, 0)
    line_points = [[30, 30], [30, 570]]
    surface = pygame.display.get_surface()

    for i in range(0, 19):
        pygame.draw.line(surface, black, line_points[0], line_points[1])
        line_points[0][0] += 30
        line_points[1][0] += 30


def _draw_star_points():
    black = (0, 0, 0)
    star_point_1 = (120, 120)
    star_point_2 = (300, 120)
    star_point_3 = (480, 120)
    star_point_4 = (120, 300)
    star_point_5 = (300, 300)
    star_point_6 = (480, 300)
    star_point_7 = (120, 480)
    star_point_8 = (300, 480)
    star_point_9 = (480, 480)

    star_points = [star_point_1, star_point_2, star_point_3,
                   star_point_4, star_point_5, star_point_6,
                   star_point_7, star_point_8, star_point_9]

    surface = pygame.display.get_surface()

    for star_point in star_points:
        pygame.draw.circle(surface, black, star_point, 5)
