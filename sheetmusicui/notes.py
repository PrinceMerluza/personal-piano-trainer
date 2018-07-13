from pygame import image, transform
from enum import Enum


class Note:
    """Musical note class"""

    _all_notes = {
        ('A', 'a'): 0,
        ('Bb', 'bb', 'A#', 'a#'): 1,
        ('B', 'b'): 2,
        ('C', 'c'): 3,
        ('C#', 'c#', 'Db', 'db'): 4,
        ('D', 'd'): 5,
        ('Eb', 'eb', 'D#', 'd#'): 6,
        ('E', 'e'): 7,
        ('F', 'f'): 8,
        ('F#', 'f#', 'Gb', 'gb'): 9,
        ('G', 'g'): 10,
        ('Ab', 'ab', 'G#', 'g#'): 11
    }

    @classmethod
    def tone_val_to_str(cls, tone_val):
        """
        Converts a tone integer value to the string representation
        Example: 21 --> 'A1'
        :param tone_val:
        :return:
        """
        if not 21 <= tone_val <= 108:
            raise ValueError('Value out of bounds')

        # Normalize A1 to 0
        tone = tone_val - 21

        # Get first entry in the notes tuple key.
        base_val = next(k[0] for k, v in cls._all_notes.items() if v == tone % 12)
        suffix = str((tone // 12) + 1)

        return base_val + suffix

    @classmethod
    def tone_str_to_val(cls, tone_str):
        try:
            prefix = tone_str[:-1]
            suffix = tone_str[-1]
            base_val = next(v for k, v in cls._all_notes.items() if prefix in k)
            octave_offset = 12 * (int(suffix) - 1)

            # Add 21 for the A1 offset
            return octave_offset + base_val + 21

        except (ValueError, StopIteration) as e:
            raise Exception("Invalid tone string: '{}'".format(tone_str))

    def __init__(self):
        pass

#
# _whole_note = image.load("./assets/whole-note.png")
# _half_note = image.load("./assets/half-note.png")
# _quarter_note = image.load("./assets/quarter-note.png")
#
# notes_dict = {
#     '1': _whole_note,
#     'whole': _whole_note,
#     '2': _half_note,
#     'half': _half_note,
#     '4': _quarter_note,
#     'quarter': _quarter_note
# }
#
#
# def draw_note(note_to_draw, surface, pos=(0, 0)):
#     surface.blit(notes_dict[note_to_draw], pos)
#
#
# _LINE_WIDTH = 2
#
# _offset = [0, 0]

if __name__ == '__main__':
    print(Note.tone_val_to_str(48))
    print(Note.tone_str_to_val('C3'))