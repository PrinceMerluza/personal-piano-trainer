import pygame
import math
from sys import exit
from pygame.locals import *

import notes
import staff
from style import colors


pygame.init()
screen = pygame.display.set_mode((800, 600))

notes.generate_notes_dict(0.7)

note_values = ['F', 'E', 'D', 'C', 'B', 'A']

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

    staff_pos = (30, 30)
    staff.draw_grand_staff(700, screen, staff_pos)
    draw_note_on_staff(staff_pos, 1, "F5")
    draw_note_on_staff(staff_pos, 2, "E5")
    draw_note_on_staff(staff_pos, 3, "C5")
    draw_note_on_staff(staff_pos, 4, "A5")
    draw_note_on_staff(staff_pos, 5, "C4")

    pygame.display.update()


def draw_note_on_staff(staff_pos, note_pos, note_string):
    note_value = get_note_value(note_string)
    notes.draw_note('1', screen,
                    (staff_pos[0] + (note_pos * 50), staff_pos[1] + (note_value * 15)))


def get_note_value(note_string):
    return note_values.index(note_string[0]) + ((5 - int(note_string[1])) * 7)


if __name__ == '__main__':
    main()
