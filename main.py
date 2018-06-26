import pygame
import math
from sys import exit
from pygame.locals import *

import notes
import staff
from style import colors


pygame.init()
screen = pygame.display.set_mode((800, 600))


def main():
    # Game Loop
    while True:
        event_update()
        display_update()


def event_update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


def display_update():
    screen.fill(colors['WHITE'])

    staff.draw_staff(500, screen, (20, 20))

    pygame.display.update()


if __name__ == '__main__':
    main()
