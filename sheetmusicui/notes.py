from pygame import image, transform
from enum import Enum


class NoteType(Enum):
    WHOLE = 1
    HALF = 2
    QUARTER = 4
    EIGHTH = 8
    SIXTEENTH = 16
    THIRTY_SECOND = 32


class Note:
    """
    Musical notes class.
    Notes are musical information + image(PyGame Surface) for the note.
    Display functionality should be handled by the StaffManager class.
    """
    # This is the percentage for scaling the note images and offsets
    _SCALE_DOWN = 0.2

    _all_notes = {
        ('C', 'c'): 0,
        ('C#', 'c#', 'Db', 'db'): 1,
        ('D', 'd'): 2,
        ('Eb', 'eb', 'D#', 'd#'): 3,
        ('E', 'e'): 4,
        ('F', 'f'): 5,
        ('F#', 'f#', 'Gb', 'gb'): 6,
        ('G', 'g'): 7,
        ('Ab', 'ab', 'G#', 'g#'): 8,
        ('A', 'a'): 9,
        ('Bb', 'bb', 'A#', 'a#'): 10,
        ('B', 'b'): 11,
    }

    _image_file_info = {
        NoteType.WHOLE: {
            "path": "./assets/whole-note.png",
            "offset": (107, 69)
        },
        NoteType.HALF: {
            "path": "./assets/half-note.png",
            "offset": (95, 528)
        },
        NoteType.QUARTER: {
            "path": "./assets/quarter-note.png",
            "offset": (88, 523)
        }
    }

    def __init__(self, tone=21, note_type=NoteType.WHOLE):
        """
        Initializer
        :param tone:        str or int. Represent the tone/pitch of the note. Default: 21 (A1)
        :param note_type:   NoteType. Represent the type of note (rhythm). Default: WHOLE
        """
        self._image = None
        self._note_type = None
        self._tone = None

        # Internally, tone should always be in int MIDI representation
        self.tone = tone
        print(self.tone)
        # Assign note type
        if not isinstance(note_type, NoteType):
            raise TypeError("Please use the NoteType Enum.")
        else:
            self.note_type = note_type

    @property
    def tone(self):
        return self._tone

    @tone.setter
    def tone(self, val):
        self._tone = Note.tone_val(val)

    @property
    def note_type(self):
        return self._note_type

    @note_type.setter
    def note_type(self, val):
        """When note_type is changed also update the image"""
        self._note_type = val
        self._image = image.load(Note._image_file_info[val]["path"])

    @property
    def natural_val(self):
        """
        Get the natural note (without flats or sharps)
        Will round to the sharp version.
        TODO Consider Key in order to choose natural tone
        """
        base_tone = self.tone % 12
        octave = (self.tone // 12) - 1

        # Bring down the sharp
        if base_tone in [1, 3, 6, 8, 10]:
            base_tone -= 1

        return octave * base_tone

    @property
    def image(self):
        orig_size = self._image.get_size()
        resized = transform.smoothscale(self._image, (int(orig_size[0] * Note._SCALE_DOWN),
                                                      int(orig_size[1] * Note._SCALE_DOWN)))
        return resized

    @classmethod
    def tone_val_to_str(cls, tone_val):
        """
        Converts a tone integer value to the string representation
        Example: 21 --> 'A1', 0 --> 'C0'
        :param tone_val:
        :return:
        """
        if not 12 <= tone_val <= 108:
            raise ValueError('Value out of bounds')

        # Get first entry in the notes tuple key.
        base_val = next(k[0] for k, v in cls._all_notes.items() if v == tone_val % 12)
        suffix = str((tone_val // 12) - 1)

        return base_val + suffix

    @classmethod
    def tone_str_to_val(cls, tone_str):
        """
        Convert tone string to integer value
        Example: 'C4' --> 60
        :param tone_str: The tone string
        :return:
        """
        try:
            prefix = tone_str[:-1]
            suffix = tone_str[-1]
            base_val = next(v for k, v in cls._all_notes.items() if prefix in k)
            octave_offset = 12 * (int(suffix) + 1)

            # Add 21 for the A1 offset
            return octave_offset + base_val

        except (ValueError, StopIteration) as e:
            raise Exception("Invalid tone string: '{}'".format(tone_str))

    @classmethod
    def tone_val(cls, val):
        """Returns the tone int value regardless of input"""
        if type(val) == str:
            return cls.tone_str_to_val(val)
        if type(val) == int:
            if 21 <= val <= 108:
                return val
            else:
                raise Exception("Tone out of bounds")

    def draw(self, surface, x=0, y=0):
        offset = Note._image_file_info[self.note_type]["offset"]
        offset = (int(offset[0] * Note._SCALE_DOWN), int(offset[1] * Note._SCALE_DOWN))
        surface.blit(self.image, (x - offset[0], y - offset[1]))


if __name__ == '__main__':
    print("{}".format(Note.tone_str_to_val("C0")))
    pass