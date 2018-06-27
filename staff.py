import pygame
from pygame import Rect
from style import colors

STAFF_LINE_INTERVAL = 30
STAFF_LINE_PIXEL_WIDTH = 2


def draw_staff(width, surface, start_pos=(0, 0)):
    # Draw Rectangle bounding box of staff
    pygame.draw.rect(surface,
                     colors['BLACK'],
                     Rect(start_pos, (width, STAFF_LINE_INTERVAL * 4)),
                     STAFF_LINE_PIXEL_WIDTH)
    # Draw Inner Lines
    for i in range(1, 4):
        pygame.draw.line(surface,
                         colors['BLACK'],
                         (start_pos[0],
                          start_pos[1] + STAFF_LINE_INTERVAL * i),
                         (start_pos[0] + width,
                          start_pos[1] + STAFF_LINE_INTERVAL * i),
                         STAFF_LINE_PIXEL_WIDTH)
