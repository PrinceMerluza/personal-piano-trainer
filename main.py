import pygame
import notes
from style import colors
import math
from sys import exit
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((800, 600))


STAFF_LINE_INTERVAL = 30
STAFF_LINE_PIXEL_WIDTH = 2


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

    draw_staff(500, (20, 20))

    pygame.display.update()


def draw_staff(width, start_pos=(0, 0)):
    # Draw Rectangle bounding box of staff
    pygame.draw.rect(screen,
                     colors['BLACK'],
                     Rect(start_pos, (width, STAFF_LINE_INTERVAL * 4)),
                     STAFF_LINE_PIXEL_WIDTH)
    # Draw Inner Lines
    for i in range(1, 4):
        pygame.draw.line(screen,
                         colors['BLACK'],
                         (start_pos[0],
                          start_pos[1] + STAFF_LINE_INTERVAL * i),
                         (start_pos[0] + width,
                          start_pos[1] + STAFF_LINE_INTERVAL * i),
                         STAFF_LINE_PIXEL_WIDTH)


if __name__ == '__main__':
    main()
