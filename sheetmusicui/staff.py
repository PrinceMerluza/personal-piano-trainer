import pygame
from pygame import Rect, transform, image
from style import colors
from sheetmusicui import notes


STAFF_LINE_INTERVAL = 30    # Pixel interval between staff lines
STAFF_LINE_PIXEL_WIDTH = 2  # Width in Pixel of staff line

TREBLE_CLEF_FILE = "./assets/treble-clef.png"
BASS_CLEF_FILE = "./assets/bass-clef.png"

_existing_notes = []


def add_note(note_to_add):
    _existing_notes.append(note_to_add)


def draw_notes(surface):
    for note in _existing_notes:
        notes.draw_note()


def draw_staff(width, surface, start_pos=(0, 0), type=None):
    """
    Draws a staff to the screen
    :param width:       Int. Width of staff in pixels
    :param surface:     Pygame surface to draw on
    :param start_pos:   Tuple. Starting Position in pixels
    :param  type:       String. 'treble' or 'bass' type
    :return: None
    """
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

    # Draw the clefs
    if type == 'treble':
        clef = image.load(TREBLE_CLEF_FILE)
        original_size = clef.get_size()
        clef = transform.smoothscale(clef, (int(original_size[0] * 0.13),
                                            int(original_size[1] * 0.13)))
        surface.blit(clef, (start_pos[0], start_pos[1] - 20))
    elif type == 'bass':
        clef = image.load(BASS_CLEF_FILE)
        original_size = clef.get_size()
        clef = transform.smoothscale(clef, (int(original_size[0] * 0.2),
                                            int(original_size[1] * 0.2)))
        surface.blit(clef, (start_pos[0], start_pos[1] + 10))
    else:
        pass


def draw_grand_staff(width, surface, start_pos=(0, 0)):
    """
    Draw the treble and the bass staff
    :param width:
    :param surface:
    :param start_pos:
    :return:
    """
    draw_staff(width, surface, start_pos, 'treble')
    draw_staff(width, surface, (start_pos[0], 180 + start_pos[1]), 'bass')
