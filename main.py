import pygame
import math
from sys import exit
from pygame import Color, Rect
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((800, 600))

colors = {
    'BLACK': Color(0, 0, 0),
    'WHITE': Color(255, 255, 255),
    'MAGENTA': Color(255, 0, 255),
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
    screen.fill(colors['WHITE'])

    draw_staff(500, (20, 20))
    fill_notes_dict(0.75)

    draw_note('32', screen)
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
    note_width = 100 * scale
    note_height = 125 * scale
    note_size = (note_width, note_height)

    notes_dict.setdefault('1', generate_whole_note(note_size))
    notes_dict.setdefault('2', generate_half_note(note_size))
    notes_dict.setdefault('4', generate_quarter_note(note_size))
    notes_dict.setdefault('8', generate_eighth_note(note_size))
    notes_dict.setdefault('16', generate_sixteenth_note(note_size))
    notes_dict.setdefault('32', generate_thirty_second_note(note_size))


# Returns pygame surface of a whole note
def generate_whole_note(note_size, filled=False):
    note_width = note_size[0]
    note_height = note_size[1]
    note = pygame.Surface(note_size)
    note.fill(colors['MAGENTA'])
    note.set_colorkey(colors['MAGENTA'])
    pygame.draw.ellipse(note,
                        colors['BLACK'],
                        Rect((0, (2 * note_height) / 3),
                             (note_width / 2, note_height / 3)),
                        # Decision for filling based on note being built
                        STAFF_LINE_PIXEL_WIDTH if not filled else 0)
    return note


def generate_half_note(note_size):
    note_width = note_size[0]
    note_height = note_size[1]
    note = pygame.Surface(note_size)
    note.fill(colors['MAGENTA'])
    note.set_colorkey(colors['MAGENTA'])
    note.blit(generate_whole_note(note_size), (0, 0))
    pygame.draw.line(note,
                     colors['BLACK'],
                     (note_width / 2.1, (5 * note_height) / 6),
                     (note_width / 2.1, 0),
                     STAFF_LINE_PIXEL_WIDTH)
    return note


def generate_quarter_note(note_size):
    note_width = note_size[0]
    note_height = note_size[1]
    note = pygame.Surface(note_size)
    note.fill(colors['MAGENTA'])
    note.set_colorkey(colors['MAGENTA'])
    note.blit(generate_whole_note(note_size, True), (0, 0))
    pygame.draw.line(note,
                     colors['BLACK'],
                     (note_width / 2.1, (5 * note_height) / 6),
                     (note_width / 2.1, 0),
                     STAFF_LINE_PIXEL_WIDTH)
    return note


def generate_eighth_note(note_size):
    note_width = note_size[0]
    note_height = note_size[1]
    note = pygame.Surface(note_size)
    note.fill(colors['MAGENTA'])
    note.set_colorkey(colors['MAGENTA'])
    note.blit(generate_quarter_note(note_size), (0, 0))
    pygame.draw.line(note,
                     colors['BLACK'],
                     (note_width / 2.1, 0),
                     (note_width, note_height / 8),
                     int(STAFF_LINE_PIXEL_WIDTH * 3))
    return note


def generate_sixteenth_note(note_size):
    note_width = note_size[0]
    note_height = note_size[1]
    note = pygame.Surface(note_size)
    note.fill(colors['MAGENTA'])
    note.set_colorkey(colors['MAGENTA'])
    note.blit(generate_eighth_note(note_size), (0, 0))
    pygame.draw.line(note,
                     colors['BLACK'],
                     (note_width / 2.1, note_height / 8),
                     (note_width, (note_height / 8) * 2),
                     int(STAFF_LINE_PIXEL_WIDTH * 3))
    return note


def generate_thirty_second_note(note_size):
    note_width = note_size[0]
    note_height = note_size[1]
    note = pygame.Surface(note_size)
    note.fill(colors['MAGENTA'])
    note.set_colorkey(colors['MAGENTA'])
    note.blit(generate_sixteenth_note(note_size), (0, 0))
    pygame.draw.line(note,
                     colors['BLACK'],
                     (note_width / 2.1, (note_height / 8) * 2),
                     (note_width, (note_height / 8) * 3),
                     int(STAFF_LINE_PIXEL_WIDTH * 3))
    return note


def draw_note(note_to_draw, surface, pos=(0, 0)):
    surface.blit(notes_dict[note_to_draw], pos)


if __name__ == '__main__':
    main()
