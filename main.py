import pygame
from sys import exit
from pygame import Color, Rect
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((800, 600))

colors = {
    'BLACK': Color(0, 0, 0),
    'WHITE': Color(255, 255, 255),
}

STAFF_LINE_INTERVAL = 30
STAFF_LINE_PIXEL_WIDTH = 2

notes_dict = {}

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
    screen.fill(Color(255, 255, 255))

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


def fill_notes_dict(scale=1.0):
    note_width = 200 * scale
    note_height = 300 * scale
    note_size = (note_width, note_height)

    whole_note = pygame.Surface(note_size)
    pygame.draw.ellipse(whole_note,
                        colors['BLACK'],
                        Rect((0, (2 * note_height) / 3),
                            (note_width / 2, note_height / 3)),
                        STAFF_LINE_PIXEL_WIDTH)
    notes_dict.setdefault('whole_note', whole_note)


if __name__ == '__main__':
    main()
