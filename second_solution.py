import sys

import pygame

width = 1000
high = 700
squere_size = 50
left_and_top_border = 1
right_border = width - squere_size - 1
down_border = high - squere_size - 1

pygame.init()

win = pygame.display.set_mode((width, high))
pygame.display.set_caption("DVD")

position_x = 100
position_y = 100


def movement_left_upper(position_x, position_y):
    while True:
        pygame.draw.rect(win, (255, 0, 255), (position_x, position_y, squere_size, squere_size))

        pygame.display.update()
        win.fill((0, 0, 0))
        if position_y == 0 or position_y == high - squere_size or position_x == 0 or position_x == width - squere_size:
            return position_x + 1, position_y + 1
        position_x = position_x - 1
        position_y = position_y - 1


def movement_right_upper(position_x, position_y):
    while True:
        pygame.draw.rect(win, (255, 255, 0), (position_x, position_y, squere_size, squere_size))

        pygame.display.update()
        win.fill((0, 0, 0))

        if position_y == 0 or position_y == high - squere_size or position_x == 0 or position_x == width - squere_size:
            return position_x - 1, position_y + 1
        position_x = position_x + 1
        position_y = position_y - 1


def movement_left_down(position_x, position_y):
    while True:
        pygame.draw.rect(win, (223, 255, 255), (position_x, position_y, squere_size, squere_size))

        pygame.display.update()
        win.fill((0, 0, 0))
        if position_y == 0 or position_y == high - squere_size or position_x == 0 or position_x == width - squere_size:
            return position_x + 1, position_y - 1
        position_x = position_x - 1
        position_y = position_y + 1


def movement_right_down(position_x, position_y):
    while True:
        pygame.draw.rect(win, (255, 111, 255), (position_x, position_y, squere_size, squere_size))

        pygame.display.update()
        win.fill((0, 0, 0))
        if position_y == 0 or position_y == high - squere_size or position_x == 0 or position_x == width - squere_size:
            return position_x - 1, position_y - 1
        position_x = position_x + 1
        position_y = position_y + 1


def application_closing_service():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def change_direction(direction):
    if direction == "right_down_direction" and position_y == down_border:  direction = "right_upper_direction"

    if direction == "right_down_direction" and position_x == right_border: direction = "left_down_direction"

    if direction == "right_upper_direction" and position_y == left_and_top_border: direction = "right_down_direction"

    if direction == "right_upper_direction" and position_x == right_border: direction = "left_upper_direction"

    if direction == "left_upper_direction" and position_y == left_and_top_border: direction = "left_down_direction"

    if direction == "left_upper_direction" and position_x == left_and_top_border: direction = "right_upper_direction"

    if direction == "left_down_direction" and position_y == down_border: direction = "left_upper_direction"

    if direction == "left_down_direction" and position_x == left_and_top_border: direction = "right_down_direction"

    return direction


def choice_of_direction(position_x, position_y):
    match direction:

        case "left_upper_direction":
            position_x, position_y = movement_left_upper(position_x, position_y)
        case "right_upper_direction":
            position_x, position_y = movement_right_upper(position_x, position_y)
        case "left_down_direction":
            position_x, position_y = movement_left_down(position_x, position_y)
        case "right_down_direction":
            position_x, position_y = movement_right_down(position_x, position_y)
    return position_x, position_y


direction = "right_down_direction"
while True:
    application_closing_service()
    direction = change_direction(direction)
    position_x, position_y = choice_of_direction(position_x, position_y)

    pygame.display.update()
