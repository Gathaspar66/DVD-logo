import sys

import pygame

width = 1000
high = 600
pygame.init()

win = pygame.display.set_mode((width, high))
pygame.display.set_caption("DVD")
clock = pygame.time.Clock()

logo = pygame.image.load("orange.png")
square = logo.get_rect()

fps = 60

a = 10
b = 10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if square.left < 0:
        a = -a
        logo = pygame.image.load("orange.png")

    if square.right > width:
        a = -a
        logo = pygame.image.load("blue.png")

    if square.top < 0:
        b = -b
        logo = pygame.image.load("red.png")
    if square.bottom > high:
        b = -b
        logo = pygame.image.load("purple.png")

    square.left = square.left + a
    square.top = square.top + b

    win.blit(logo, square)
    pygame.display.update()
    win.fill((0, 0, 0))
    clock.tick(fps)
