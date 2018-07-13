from pygame import image, transform


_whole_note = image.load("./assets/whole-note.png")
_half_note = image.load("./assets/half-note.png")
_quarter_note = image.load("./assets/quarter-note.png")

notes_dict = {
    '1': _whole_note,
    'whole': _whole_note,
    '2': _half_note,
    'half': _half_note,
    '4': _quarter_note,
    'quarter': _quarter_note
}


def draw_note(note_to_draw, surface, pos=(0, 0)):
    surface.blit(notes_dict[note_to_draw], pos)


_LINE_WIDTH = 2

_offset = [0, 0]
