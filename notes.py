import pygame
from pygame import Rect
from style import colors

_notes_dict = {}

_LINE_WIDTH = 2

_offset = (0, 0)


def generate_notes_dict(scale=1.0):
    note_width = 100 * scale
    note_height = 125 * scale
    note_size = (note_width, note_height)
    _offset[0] = int(note_width * (1.0 / 4.0))
    _offset[1] = int(note_height * (5.0 / 6.0))

    _notes_dict.setdefault('1', _generate_whole_note(note_size))
    _notes_dict.setdefault('2', _generate_half_note(note_size))
    _notes_dict.setdefault('4', _generate_quarter_note(note_size))
    _notes_dict.setdefault('8', _generate_eighth_note(note_size))
    _notes_dict.setdefault('16', _generate_sixteenth_note(note_size))
    _notes_dict.setdefault('32', _generate_thirty_second_note(note_size))


def get_offset():
    return _offset


def _generate_whole_note(note_size, filled=False):
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
                        _LINE_WIDTH if not filled else 0)
    return note


def _generate_half_note(note_size):
    note_width = note_size[0]
    note_height = note_size[1]
    note = pygame.Surface(note_size)
    note.fill(colors['MAGENTA'])
    note.set_colorkey(colors['MAGENTA'])
    note.blit(_generate_whole_note(note_size), (0, 0))
    pygame.draw.line(note,
                     colors['BLACK'],
                     (note_width / 2.1, (5 * note_height) / 6),
                     (note_width / 2.1, 0),
                     _LINE_WIDTH)
    return note


def _generate_quarter_note(note_size):
    note_width = note_size[0]
    note_height = note_size[1]
    note = pygame.Surface(note_size)
    note.fill(colors['MAGENTA'])
    note.set_colorkey(colors['MAGENTA'])
    note.blit(_generate_whole_note(note_size, True), (0, 0))
    pygame.draw.line(note,
                     colors['BLACK'],
                     (note_width / 2.1, (5 * note_height) / 6),
                     (note_width / 2.1, 0),
                     _LINE_WIDTH)
    return note


def _generate_eighth_note(note_size):
    note_width = note_size[0]
    note_height = note_size[1]
    note = pygame.Surface(note_size)
    note.fill(colors['MAGENTA'])
    note.set_colorkey(colors['MAGENTA'])
    note.blit(_generate_quarter_note(note_size), (0, 0))
    pygame.draw.line(note,
                     colors['BLACK'],
                     (note_width / 2.1, 0),
                     (note_width, note_height / 8),
                     int(_LINE_WIDTH * 3))
    return note


def _generate_sixteenth_note(note_size):
    note_width = note_size[0]
    note_height = note_size[1]
    note = pygame.Surface(note_size)
    note.fill(colors['MAGENTA'])
    note.set_colorkey(colors['MAGENTA'])
    note.blit(_generate_eighth_note(note_size), (0, 0))
    pygame.draw.line(note,
                     colors['BLACK'],
                     (note_width / 2.1, note_height / 8),
                     (note_width, (note_height / 8) * 2),
                     int(_LINE_WIDTH * 3))
    return note


def _generate_thirty_second_note(note_size):
    note_width = note_size[0]
    note_height = note_size[1]
    note = pygame.Surface(note_size)
    note.fill(colors['MAGENTA'])
    note.set_colorkey(colors['MAGENTA'])
    note.blit(_generate_sixteenth_note(note_size), (0, 0))
    pygame.draw.line(note,
                     colors['BLACK'],
                     (note_width / 2.1, (note_height / 8) * 2),
                     (note_width, (note_height / 8) * 3),
                     int(_LINE_WIDTH * 3))
    return note


def draw_note(note_to_draw, surface, pos=(0, 0)):
    surface.blit(_notes_dict[note_to_draw], (pos[0] - _offset[0], pos[1] - _offset[1]))