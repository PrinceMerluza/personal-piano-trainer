import pygame
import random
from sys import exit
from pygame.locals import *
import pygame.midi

from sheetmusicui import notes, staff
from sheetmusicui.style import colors


pygame.init()
pygame.midi.init()

screen = pygame.display.set_mode((800, 600))

#notes.generate_notes_dict(0.7)

note_values = ['G', 'F', 'E', 'D', 'C', 'B', 'A']
all_notes = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab"]

midi_input_id = pygame.midi.get_default_input_id()
midi_input = False
if midi_input_id != -1:
    midi_input = pygame.midi.Input(midi_input_id)

practice_notes = ["C4", "D4", "E4", "F4", "G4", "C3", "D3", "E3", "F3", "G3"]

key_pressed = -1

test_note = ""


def main():
    staff_manager = staff.StaffManager()
    staff_manager.init_grand_staff(width=750, x=20, y=50)

    screen.fill(colors['WHITE'])
    # staff_manager.add_note("G5", "E5", "C5", "A4", "F4", "D4",
    #                        "B3", "G3", "E3", "C3", "A2", "F2")
    staff_manager.add_note('A5', 'F5', 'D5', 'B4', 'G4', 'E4', 'C4',
                           'A3', 'F3', 'D3', 'B2', 'G2', 'E2')
    staff_manager.draw(screen)

    # note = notes.Note(21, notes.NoteType.HALF)
    # print(note.image)
    # note.draw(screen, 150, 110)
    # random_test_note()

    pygame.display.update()
    # Game Loop
    while True:
        event_update()
        # display_update()
    #
    #    if key_pressed == test_note:
    #        random_test_note()


def event_update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            pygame.midi.quit()
            exit()

    if midi_input:
        for midi_event in midi_input.read(2):
            if midi_event[0][0] == 144:
                pressed_key(midi_event[0][1])


# def display_update():
#     global test_note
#     screen.fill(colors['WHITE'])
#
#     staff_pos = (30, 30)
#     staff.draw_grand_staff(700, screen, staff_pos)
#     draw_note_on_staff(staff_pos, 1, test_note)
#
#     pygame.display.update()


def pressed_key(key):
    global key_pressed
    key_pressed = midi_value_to_note_string(key)


def random_test_note():
    global test_note
    test_note = practice_notes[random.randint(0, len(practice_notes) - 1)]
    print(test_note)


def draw_note_on_staff(staff_pos, note_pos, note_string):
    note_value = note_string_to_coordinates(note_string)
    notes.draw_note('1', screen,
                    (staff_pos[0] + (note_pos * 50), (staff_pos[-1] + (note_value * 15) - 15)))


def note_string_to_coordinates(note_string):
    return note_values.index(note_string[0]) + ((5 - int(note_string[1])) * 7)


def midi_value_to_note_string(midi_value):
    midi_value -= 21
    return all_notes[midi_value % 12] + str((midi_value // 12) + 1)


if __name__ == '__main__':
    main()
